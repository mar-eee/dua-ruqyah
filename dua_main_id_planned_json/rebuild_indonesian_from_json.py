#!/usr/bin/env python3
"""Rebuild dua_main_id.sqlite from the planned Indonesian JSON workspace."""

import argparse
import base64
import json
import sqlite3
from pathlib import Path


def q(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def sqlite_value(value):
    if isinstance(value, dict) and set(value) == {"__sqlite_blob_base64__"}:
        return base64.b64decode(value["__sqlite_blob_base64__"])
    return value


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def rebuild(source_dir: Path, output: Path):
    metadata = load_json(source_dir / "_database_metadata.json")
    if output.exists():
        output.unlink()

    with sqlite3.connect(output) as connection:
        connection.execute("PRAGMA foreign_keys = OFF")
        connection.execute("BEGIN")

        for obj in metadata["schema_objects"]:
            if obj["type"] == "table":
                connection.execute(obj["sql"])

        for table in metadata["table_order"]:
            plan = metadata["table_plan"][table]
            columns = plan["columns"]
            insert_sql = (
                f"INSERT INTO {q(table)} "
                f"({', '.join(q(column) for column in columns)}) "
                f"VALUES ({', '.join('?' for _ in columns)})"
            )
            all_rows = []
            for chunk_file in plan["chunk_files"]:
                rows = load_json(source_dir / chunk_file)
                for row in rows:
                    all_rows.append(
                        tuple(sqlite_value(row.get(column)) for column in columns)
                    )
            if all_rows:
                connection.executemany(insert_sql, all_rows)

        for obj in metadata["schema_objects"]:
            if obj["type"] != "table":
                connection.execute(obj["sql"])

        if metadata.get("sqlite_sequence"):
            connection.execute("DELETE FROM sqlite_sequence")
            connection.executemany(
                "INSERT INTO sqlite_sequence(name, seq) VALUES (?, ?)",
                [(row["name"], row["seq"]) for row in metadata["sqlite_sequence"]],
            )

        pragmas = metadata.get("pragmas", {})
        connection.execute(f"PRAGMA application_id = {int(pragmas.get('application_id', 0))}")
        connection.execute(f"PRAGMA user_version = {int(pragmas.get('user_version', 0))}")
        connection.commit()

        result = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"SQLite integrity check failed: {result}")

    print(f"Indonesian SQLite created: {output}")


def main():
    source_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=source_dir.parent / "dua_main_id_rebuilt.sqlite",
        help="Output path, default: ../dua_main_id_rebuilt.sqlite",
    )
    args = parser.parse_args()
    rebuild(source_dir, args.output.resolve())


if __name__ == "__main__":
    main()
