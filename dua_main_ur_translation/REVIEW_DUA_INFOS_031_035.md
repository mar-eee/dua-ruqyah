# Urdu review: dua_infos 031–035

Five chunks cover record 18 part 10/10; records 19, 21, 22 and 23 in full; and record 20 parts 1–7/7. All 12 item-parts and 17 requested target fields are translated and marked `done`. Chunk 030 was already completed in the preceding batch and was not changed.

## Editorial and preservation checks

- Compared every target passage with its Bengali source for meaning, sequence, conditions, speaker, theological qualification, and citations; then read the Urdu as continuous prose. Named or contested fiqh and doctrinal positions remain attributed to the source author rather than stated as independently verified universal rulings.
- The 2 protected `<ar1>` spans in record 19 and the `<ar>` Quran excerpt in record 21 remain exactly as supplied. The Quran excerpt's words are from [49:10](https://quran.com/49:10); its supplied spelling/marks were not changed to match a different script convention. HTML tag order and JSON schema were preserved.
- The source's closing sentence in record 21 appears to omit a negation: it demands hostility toward someone professing faith immediately after arguing for brotherly love. Urdu renders *not maintaining such hostility*, which follows that paragraph and [Quran 49:9–10](https://quran.com/49/9-10). This editorial correction is recorded in `GLOSSARY.json`.
- The source's guidance on non-Arabic prayer in record 18 part 10 is kept as the author's cautious assessment, not made into a categorical fatwa. Uncited claims about barzakh life and prophetic attributes in record 20 are not marked independently verified.

## Citation corrections

| Record | Bengali source | Urdu and evidence |
|---|---|---|
| 19 | al-Zukhruf `1` is listed among passages where the polytheists acknowledge Allah as Creator. | Corrected to [43:87](https://quran.com/43:87); [43:1](https://quran.com/43:1) does not carry that statement. |
| 20, part 6 | Bukhari `13445` is attached to the warning against exaggerated praise of the Prophet ﷺ. | Corrected the apparent OCR error to [Bukhari 3445](https://sunnah.com/bukhari:3445). |
| 23 | Abu Dawud `4683` for loving, disliking, giving and withholding for Allah. | Corrected to [Abu Dawud 4681](https://sunnah.com/abudawud:4681). |
| 23 | Abu Dawud `5127` for Abu Dharr's repeated exchange. | Corrected to [Abu Dawud 5126](https://sunnah.com/abudawud:5126); [5127](https://sunnah.com/abudawud:5127) is an adjacent Anas narration. |
| 23 | Muslim `2566` is repeated for the man visiting his brother and the angel. | Kept [Muslim 2566](https://sunnah.com/muslim:2566) for the shade report; corrected the visitor-and-angel report to [Muslim 2567a](https://sunnah.com/muslim:2567a), cited as `2567` in the Urdu. |

Other checked narration anchors include [Bukhari 16](https://sunnah.com/bukhari:16) (three qualities and sweetness of faith), [Bukhari 15](https://sunnah.com/bukhari:15) (loving the Prophet ﷺ), and [Bukhari 3688](https://sunnah.com/bukhari:3688) (Anas, love, and companionship). Quran 3:31 was checked against [its verse](https://quran.com/3:31). These spot checks do not authenticate every secondary citation or source grading in the essays.

## Mechanical result and outstanding review

- `scripts/verify.py` passed for each of the five chunks, with no structure, protected-Arabic, tag, residual-source, or status errors.
- A separate part-by-part numeric multiset comparison found only the five documented source-reference corrections above; every other numeral was preserved, including edition-specific tokens.
- Record 23 has a possible OCR-damaged `al-Silsilah al-Sahihah 2/398–700` citation. It is retained rather than guessed and requires edition-level bibliographic review. The source's other unnamed grading claims were attributed, not presented as newly verified.
- This is an editorial and automated review, not scholar or native-editor sign-off. The full SQLite build remains deferred until all required chunks are complete.
