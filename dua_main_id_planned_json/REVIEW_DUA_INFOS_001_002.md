# Indonesian dua_infos 001–002 review

Scope: records 1–7, source language Bangla (dua_main_bn.sqlite), target
standard Indonesian (id-ID). Both name and description were translated for
every record. The 15-file chunk layout, row IDs, JSON keys, and all Arabic
inside the ar tags were retained.

Mechanical checks: all seven source IDs match the target IDs; 21 protected
Arabic blocks compare character for character, and honorific counts match the
source; translated fields contain no
Bengali-script characters; JSON parses; markup tags are balanced. These
checks do not establish native-speaker or scholarly review.

Quran meaning was checked selectively against Quran.com, including
[17:110](https://quran.com/id/al-isra/110/tafsirs),
[2:23](https://quran.com/id/al-baqarah/23),
[40:60](https://quran.com/id/sang-maha-pengampun/60/tafsirs),
[7:205](https://quran.com/id/al-araf/205/tafsirs),
[6:162](https://quran.com/id/al-anam/162/tafsirs),
[6:17](https://quran.com/id/al-anam/17),
[10:106–107](https://quran.com/id/yunus/106-107),
[22:11–13](https://quran.com/id/haji/11-13),
[23:51](https://quran.com/id/muminun/51/tafsirs),
[7:56](https://quran.com/id/al-araf/56/tafsirs), and
[13:11](https://quran.com/id/ar-rad/11/tafsirs).
The Indonesian prose is a translation of meaning, not a quotation claimed to
come verbatim from a published Indonesian Quran edition. Arabic was preserved
from the source, not silently replaced with a different script convention.

The Bangla source misstates the meaning of Quran 17:110 as “praising” Allah or
Ar-Rahman, while the verse speaks of calling upon Him by either name. The
Bangla meaning of Quran 6:17 omits the final clause about Allah's power when He
grants good. The Indonesian text follows the checked verse meanings; the Bangla
source remains unchanged and needs authorized correction.

Selected hadith cross-checks:
[Sahih Muslim 202](https://sunnah.com/muslim/1/405) confirms the narration
about the Prophet raising his hands for his community after reciting Ibrahim
14:35; [Sahih Bukhari 1013](https://sunnah.com/bukhari:1013) confirms the rain
prayer narrative. Most other hadith quotations, edition-dependent numbers,
grading claims, and source Arabic excerpts have **not** received a complete
source-by-source review. In particular, the source's ruling on reciting
Quranic verses during sujud in record 3 was rendered narrowly as a prohibition
of Quran recitation as tilawah; this interpretation needs scholarly review.

Do not label these two files fully quotation-verified or human-reviewed.
Progress and the next record are in [translation_progress.json](translation_progress.json).
