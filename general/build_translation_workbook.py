#!/usr/bin/env python3
"""Build and verify the mixed-source Dua & Ruqyah translation workbook."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import date
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "Dua_Ruqyah_Translation_Master.xlsx"
GUIDE = HERE / "README.md"
NULL_TOKEN = "⟦SQL NULL⟧"
EMPTY_TOKEN = "⟦EMPTY STRING⟧"

# The selected source is intentional: table IDs and content do not always align
# between the four language databases. Never join rows across languages by ID.
SOURCE = {
    "book_details": "en",
    "books": "en",
    "categories": "bn",
    "drawer_item_actions": "en",
    "drawer_items": "en",
    "dua_infos": "bn",
    "duas": "bn",
    "ids": "bn",
    "ruqyah_categories": "en",
    "ruqyah_details": "en",
    "ruqyah_instants": "en",
    "ruqyah_subcategories": "en",
    "ruqyah_videos": "en",
    "sections": "en",
    "subcategories": "bn",
}

TARGET_FIELDS = {
    "book_details": ("topic_name", "description"),
    "books": ("name", "writer", "translator", "editor"),
    "categories": ("name",),
    "drawer_item_actions": ("label",),
    "drawer_items": ("title", "hero_title1", "hero_title2", "content"),
    "dua_infos": ("name", "description"),
    "duas": ("groups", "name", "content", "translation", "note"),
    "ids": (),
    "ruqyah_categories": ("name",),
    "ruqyah_details": ("topic_name", "text"),
    "ruqyah_instants": ("topic_name", "name", "content", "translation"),
    "ruqyah_subcategories": ("name",),
    "ruqyah_videos": ("name", "author"),
    "sections": ("name",),
    "subcategories": ("name",),
}

NAVY = "17324D"
BLUE = "2F5D87"
TEAL = "087E83"
LIGHT_BLUE = "EAF3FA"
LIGHT_GREEN = "EAF8EE"
LIGHT_GREY = "F2F5F7"
WHITE = "FFFFFF"
TEXT = "1C2E3A"
YELLOW = "FFF1C2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def excel_value(value):
    if value is None:
        return NULL_TOKEN
    if isinstance(value, bytes):
        raise ValueError("Unexpected BLOB column; add reversible base64 encoding")
    if isinstance(value, str):
        if value == "":
            return EMPTY_TOKEN
        if len(value) > 32767:
            raise ValueError(f"Excel cell limit exceeded: {len(value)}")
    return value


def write_literal(cell, value):
    value = excel_value(value)
    cell.value = value
    if isinstance(value, str):
        # Source text starting with '=' must never become an Excel formula.
        cell.data_type = "s"
    return cell


def open_db(lang: str):
    db = ROOT / f"dua_main_{lang}.sqlite"
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


def schema(conn, table: str):
    result = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
    cols = [x[1] for x in result]
    keys = [x[1] for x in sorted(result, key=lambda x: x[5]) if x[5]]
    if not keys:
        keys = [cols[0]]
    return cols, keys


def key_text(row, keys):
    return " | ".join(f"{k}={row[k]}" for k in keys)


def load_indonesian_dua_infos():
    folder = ROOT / "dua_main_id_planned_json" / "tables" / "dua_infos"
    records = {}
    for n in range(1, 16):
        path = folder / f"dua_infos_{n:03}.json"
        for row in json.loads(path.read_text(encoding="utf-8")):
            if row["id"] in records:
                raise ValueError(f"Duplicate Indonesian dua_infos ID {row['id']}")
            records[row["id"]] = row
    if set(records) != set(range(1, 43)):
        raise ValueError("Indonesian dua_infos does not cover IDs 1–42")
    return records


def banner(ws, title, subtitle, last_col):
    last = get_column_letter(max(last_col, 5))
    ws.merge_cells(f"A1:{last}1")
    ws.merge_cells(f"A2:{last}2")
    ws["A1"] = title
    ws["A2"] = subtitle
    ws["A1"].font = Font(name="Aptos Display", size=19, bold=True, color=WHITE)
    ws["A2"].font = Font(name="Aptos", size=11, color=WHITE)
    for row in (1, 2):
        for cell in ws[row][: max(last_col, 5)]:
            cell.fill = PatternFill("solid", fgColor=NAVY)
    ws.row_dimensions[1].height = 34
    ws.row_dimensions[2].height = 27
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True


def style_header(cell, target=False):
    cell.fill = PatternFill("solid", fgColor=TEAL if target else BLUE)
    cell.font = Font(name="Aptos", size=10, bold=True, color=WHITE)
    cell.alignment = Alignment(vertical="center", wrap_text=True)
    cell.border = Border(bottom=Side(style="medium", color=NAVY))


def style_body(cell, target=False, key=False, alt=False):
    bg = LIGHT_GREEN if target else LIGHT_BLUE if key else LIGHT_GREY if alt else WHITE
    cell.fill = PatternFill("solid", fgColor=bg)
    cell.font = Font(name="Aptos", size=10, color=TEXT)
    cell.alignment = Alignment(vertical="top", wrap_text=True)


def table_sheet(wb, table, conn, id_records):
    lang = SOURCE[table]
    cols, keys = schema(conn, table)
    targets = [f"id_{x}" for x in TARGET_FIELDS[table]]
    headers = ["source_record_key", "source_language", *cols, *targets, "translation_status"]
    ws = wb.create_sheet(table)
    ws.sheet_properties.tabColor = TEAL if lang == "bn" else BLUE
    banner(ws, table.replace("_", " ").title(),
           f"Source: {lang.upper()} database  •  Original fields retained  •  Indonesian fields are green  •  SQL NULL = {NULL_TOKEN}; empty text = {EMPTY_TOKEN}",
           len(headers))
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=len(headers))
    ws.cell(3, 1, "Edit only the green id_* columns and translation_status. Preserve Arabic and source fields exactly; see Start Here.")
    ws.cell(3, 1).font = Font(name="Aptos", size=10, italic=True, color=NAVY)
    ws.row_dimensions[3].height = 24
    for i, name in enumerate(headers, 1):
        cell = ws.cell(5, i, name)
        style_header(cell, target=name.startswith("id_") or name == "translation_status")
    ws.row_dimensions[5].height = 34

    count = 0
    filled = 0
    for row in conn.execute(f'SELECT * FROM "{table}" ORDER BY ' + ", ".join(f'"{k}"' for k in keys)):
        count += 1
        xrow = 5 + count
        values = [key_text(row, keys), lang, *(row[c] for c in cols)]
        if table == "dua_infos":
            target = id_records[row["id"]]
            values.extend(target[c] for c in TARGET_FIELDS[table])
            filled += 1
            status = "assistant_checked"
        else:
            values.extend(NULL_TOKEN if row[c] is None else "" for c in TARGET_FIELDS[table])
            status = "not_started"
        values.append(status)
        for col, value in enumerate(values, 1):
            cell = write_literal(ws.cell(xrow, col), value)
            style_body(cell, target=(col > 2 + len(cols)), key=(col <= 2 or headers[col - 1] in keys), alt=count % 2 == 0)
        ws.row_dimensions[xrow].height = 58 if any(isinstance(v, str) and len(v) > 160 for v in values) else 29

    if count == 0:
        ws.cell(6, 1, "No rows in the selected source database.")
        ws.cell(6, 1).font = Font(italic=True, color=NAVY)
    ws.freeze_panes = "D6"
    ws.auto_filter.ref = f"A5:{get_column_letter(len(headers))}{max(6, 5 + count)}"
    ws.print_title_rows = "1:5"
    ws.sheet_view.zoomScale = 85
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 18
    for i, name in enumerate(headers[2:], 3):
        col = get_column_letter(i)
        ws.column_dimensions[col].width = (68 if name in ("description", "text", "content", "translation", "note", "groups", "id_description", "id_text", "id_content", "id_translation", "id_note", "id_groups") else 27)
    validator = DataValidation(type="list", formula1='"not_started,draft,assistant_checked,human_reviewed,needs_review"')
    validator.promptTitle = "Translation status"
    validator.prompt = "Choose the actual status; assistant_checked does not mean human approved."
    validator.showInputMessage = True
    ws.add_data_validation(validator)
    status_col = get_column_letter(len(headers))
    validator.add(f"{status_col}6:{status_col}{max(6, 5 + count)}")
    return count, filled, cols, keys


def start_sheet(wb, counts, provenance):
    ws = wb.active
    ws.title = "Start Here"
    ws.sheet_properties.tabColor = NAVY
    banner(ws, "Dua & Ruqyah · Translation Master",
           "One Excel workbook for every database table · source rows are preserved · Indonesian targets are editable", 7)
    lines = [
        ("Purpose", "Translate from the requested source language without mixing unrelated records that share an ID."),
        ("Bengali source", "categories, subcategories, duas, dua_infos; ids is a structural Bengali table."),
        ("English source", "All ruqyah tables, books, book_details, sections, and drawer tables."),
        ("How to work", "Open a table tab; filter by translation_status; edit only green id_* cells; keep row keys, IDs, Arabic, and original fields unchanged."),
        ("Indonesian progress", "dua_infos 42/42 is prefilled from the Indonesian JSON workspace. Other green fields are blank; a blank is not a completed translation."),
        ("NULL vs empty", f"{NULL_TOKEN} means SQL NULL; {EMPTY_TOKEN} means an empty string. A blank Indonesian cell means pending work. Keep both tokens unchanged."),
        ("Long text", "All source and prefilled target cells fit within Excel's 32,767-character limit. Row height is compact for navigation; click a cell to read its full value in the formula bar."),
        ("Nested duas", "duas.groups contains complete nested JSON in the source cell. Translate all user-visible nested text before marking the row complete."),
        ("Mismatch warning", "The four databases do not contain identical row sets. Coverage shows counts. No records are joined by matching ID across languages."),
        ("Review warning", "Assistant-checked translation is not native-speaker or scholarly approval. Check Quran, hadith, and Arabic against their sources before publication."),
        ("Rebuild", "Run `python general/build_translation_workbook.py` after the source databases or Indonesian dua_infos JSON change. This rebuilds the workbook from those sources."),
        ("Source snapshot", "See Provenance for database SHA-256 hashes and Coverage for selected source and row counts."),
    ]
    ws["A4"], ws["B4"] = "Topic", "Instruction"
    style_header(ws["A4"])
    style_header(ws["B4"])
    for n, (title, value) in enumerate(lines, 5):
        ws.cell(n, 1, title)
        ws.cell(n, 2, value)
        style_body(ws.cell(n, 1), key=True)
        style_body(ws.cell(n, 2))
        ws.row_dimensions[n].height = 47 if len(value) > 130 else 34
    ws.column_dimensions["A"].width = 27
    ws.column_dimensions["B"].width = 110
    for c in "CDEFG":
        ws.column_dimensions[c].width = 7
    ws.freeze_panes = "B5"
    ws.sheet_view.zoomScale = 95
    ws["A19"] = "Open Coverage →"
    ws["A19"].hyperlink = "#'Coverage'!A1"
    ws["A19"].font = Font(color=TEAL, bold=True, underline="single")


def coverage_sheet(wb, counts, all_counts):
    ws = wb.create_sheet("Coverage", 1)
    ws.sheet_properties.tabColor = "E4B94D"
    banner(ws, "Table coverage & source routing",
           "A count mismatch is visible, not filled with another language's rows. Click a table to inspect its complete selected-source records.", 9)
    headers = ["Table", "Selected source", "Workbook rows", "BN rows", "EN rows", "JP rows", "UR rows", "Indonesian filled", "Coverage note"]
    for col, value in enumerate(headers, 1):
        style_header(ws.cell(5, col, value))
    ws.row_dimensions[5].height = 33
    for n, table in enumerate(SOURCE, 6):
        selected_count, id_filled, _, _ = counts[table]
        note = ""
        if table == "dua_infos":
            note = "BN 42 is the structural master; EN 16 is a different dataset. Indonesian 42/42 is assistant-checked."
        elif table == "books":
            note = "English book list has 2 rows; Bengali has 3. No Bengali book was substituted."
        elif table == "book_details":
            note = "English book details have 40 rows; Bengali has 86. Extra Bengali details are not silently added."
        elif table == "ruqyah_videos":
            note = "English has 40 video rows; Bengali has 74. Requested English source used."
        elif table.startswith("ruqyah") and len(set(all_counts[lang][table] for lang in all_counts)) > 1:
            note = "Language databases differ in row count; selected English rows are preserved."
        elif table == "drawer_items":
            note = "English drawer IDs differ from Bengali IDs. Do not merge them by ID."
        row = [table, SOURCE[table].upper(), selected_count, *(all_counts[l][table] for l in ("bn", "en", "jp", "ur")), id_filled, note]
        for col, value in enumerate(row, 1):
            cell = write_literal(ws.cell(n, col), value)
            style_body(cell, key=(col <= 2), alt=n % 2 == 0)
        ws.cell(n, 1).hyperlink = f"#'{table}'!A1"
        ws.cell(n, 1).font = Font(name="Aptos", color=TEAL, underline="single", bold=True)
        ws.row_dimensions[n].height = 39 if note else 27
    for col in "BCDEFGH":
        ws.column_dimensions[col].width = 19
    ws.column_dimensions["A"].width = 27
    ws.column_dimensions["I"].width = 86
    ws.freeze_panes = "C6"
    ws.auto_filter.ref = f"A5:I{5 + len(SOURCE)}"
    ws.sheet_view.zoomScale = 90


def provenance_sheet(wb, provenance):
    ws = wb.create_sheet("Provenance", 2)
    ws.sheet_properties.tabColor = "9D83B6"
    banner(ws, "Source provenance",
           "Hashes identify the exact SQLite snapshots used to construct this workbook.", 5)
    for col, value in enumerate(("Language", "Database", "SHA-256", "Use in workbook", "Generated"), 1):
        style_header(ws.cell(5, col, value))
    for n, (lang, digest) in enumerate(provenance.items(), 6):
        values = [lang.upper(), f"dua_main_{lang}.sqlite", digest,
                  "Selected source for some table tabs" if lang in ("bn", "en") else "Coverage counts only", date.today().isoformat()]
        for col, value in enumerate(values, 1):
            style_body(write_literal(ws.cell(n, col), value), alt=n % 2 == 0)
    for col, width in zip("ABCDE", (16, 29, 72, 39, 19)):
        ws.column_dimensions[col].width = width
    ws.freeze_panes = "C6"


def guide_sheet(wb):
    raw = GUIDE.read_text(encoding="utf-8")
    if len(raw) > 32767:
        raise ValueError("Guide Markdown exceeds Excel cell limit")
    ws = wb.create_sheet("Guide Markdown")
    ws.sheet_properties.tabColor = "A0B0BA"
    banner(ws, "Workbook guide · exact Markdown copy",
           "Cell B4 contains the complete, unmodified Markdown from general/README.md. Column A presents it line by line.", 4)
    ws["A4"] = "Readable lines"
    ws["B4"] = "Exact Markdown copy"
    style_header(ws["A4"])
    style_header(ws["B4"])
    write_literal(ws["B5"], raw)
    style_body(ws["B5"])
    ws["B5"].alignment = Alignment(vertical="top", wrap_text=True)
    for n, line in enumerate(raw.splitlines(), 5):
        cell = write_literal(ws.cell(n, 1), line)
        style_body(cell, alt=n % 2 == 0)
        if line.startswith("#"):
            cell.font = Font(name="Aptos", size=12, bold=True, color=NAVY)
        ws.row_dimensions[n].height = 30 if line else 18
    ws.column_dimensions["A"].width = 110
    ws.column_dimensions["B"].width = 70
    ws.column_dimensions["C"].width = 8
    ws.column_dimensions["D"].width = 8
    ws.freeze_panes = "A5"


def verify(output, counts, connections, id_records):
    wb = load_workbook(output, read_only=False, data_only=False)
    assert set(wb.sheetnames) == set(SOURCE) | {"Start Here", "Coverage", "Provenance", "Guide Markdown"}
    assert wb["Guide Markdown"]["B5"].value == GUIDE.read_text(encoding="utf-8")
    for table, lang in SOURCE.items():
        ws = wb[table]
        conn = connections[lang]
        cols, keys = schema(conn, table)
        rows = list(conn.execute(f'SELECT * FROM "{table}" ORDER BY ' + ", ".join(f'"{k}"' for k in keys)))
        assert len(rows) == counts[table][0]
        for n, row in enumerate(rows, 6):
            expected = [key_text(row, keys), lang, *(excel_value(row[c]) for c in cols)]
            actual = [ws.cell(n, i).value for i in range(1, len(expected) + 1)]
            assert actual == expected, (table, n, "source cell mismatch")
            if table == "dua_infos":
                target = id_records[row["id"]]
                assert ws.cell(n, 3 + len(cols)).value == target["name"]
                assert ws.cell(n, 4 + len(cols)).value == target["description"]
        assert not any(cell.data_type == "f" for row in ws for cell in row)
    wb.close()


def main():
    id_records = load_indonesian_dua_infos()
    connections = {lang: open_db(lang) for lang in ("bn", "en", "jp", "ur")}
    try:
        all_counts = {lang: {t: c.execute(f'SELECT count(*) FROM "{t}"').fetchone()[0] for t in SOURCE}
                      for lang, c in connections.items()}
        provenance = {lang: sha256(ROOT / f"dua_main_{lang}.sqlite") for lang in connections}
        wb = Workbook()
        wb.properties.title = "Dua & Ruqyah Translation Master"
        wb.properties.subject = "Mixed Bengali and English source workbook for Indonesian translation"
        wb.properties.creator = "Dua & Ruqyah translation workspace"
        counts = {t: table_sheet(wb, t, connections[SOURCE[t]], id_records) for t in SOURCE}
        start_sheet(wb, counts, provenance)
        coverage_sheet(wb, counts, all_counts)
        provenance_sheet(wb, provenance)
        guide_sheet(wb)
        wb.active = 0
        wb.save(OUTPUT)
        wb.close()
        verify(OUTPUT, counts, connections, id_records)
        print(f"Workbook verified: {OUTPUT}")
        print(f"Table tabs: {len(SOURCE)}; selected-source rows: {sum(c[0] for c in counts.values())}; Indonesian dua_infos: {counts['dua_infos'][1]}/42")
    finally:
        for conn in connections.values():
            conn.close()


if __name__ == "__main__":
    main()
