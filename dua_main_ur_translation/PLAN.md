# Translation Plan

Tick a file off when `verify.py` passes on it. Work top to bottom: the small
tables settle the vocabulary that the long prose then has to match.

Budget 6000 source characters per file, max 50 rows, big rows split at paragraph boundaries.

| | Table | Files | Rows | Source chars | Source |
|---|---|---:|---:|---:|---|
| [x] | `categories` | 1 | 44 | 461 | EN |
| [ ] | `ruqyah_categories` | 1 | 15 | 312 | EN |
| [ ] | `sections` | 1 | 21 | 846 | EN |
| [x] | `subcategories` | 3 | 118 | 3,531 | EN |
| [ ] | `ruqyah_subcategories` | 4 | 163 | 4,805 | EN |
| [ ] | `ruqyah_videos` | 2 | 74 | 3,884 | BN |
| [ ] | `drawer_items` | 2 | 6 | 8,243 | BN |
| [ ] | `duas` | 64 | 1001 | 363,081 | EN |
| [ ] | `ruqyah_instants` | 20 | 308 | 112,037 | EN |
| [ ] | `ruqyah_details` | 95 | 200 | 457,751 | EN |
| [ ] | `dua_infos` | 70 | 42 | 357,024 | BN |
| | **total** | **263** | **1992** | **1,311,975** | |

---

## `categories`

Source: **EN** · fields: `name` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [x] | `work/categories/categories_001.json` | 44 | 1-44 | 461 | 44 |

## `ruqyah_categories`

Source: **EN** · fields: `name` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/ruqyah_categories/ruqyah_categories_001.json` | 15 | 1-15 | 312 | 15 |

## `sections`

Source: **EN** · fields: `name` · key: `id`, `book_id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/sections/sections_001.json` | 21 | 1-12 | 846 | 21 |

## `subcategories`

Source: **EN** · fields: `name` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [x] | `work/subcategories/subcategories_001.json` | 50 | 1-50 | 1,514 | 50 |
| [x] | `work/subcategories/subcategories_002.json` | 50 | 51-100 | 1,471 | 50 |
| [x] | `work/subcategories/subcategories_003.json` | 18 | 101-118 | 546 | 18 |

## `ruqyah_subcategories`

Source: **EN** · fields: `name` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/ruqyah_subcategories/ruqyah_subcategories_001.json` | 50 | 1-50 | 1,681 | 50 |
| [ ] | `work/ruqyah_subcategories/ruqyah_subcategories_002.json` | 50 | 51-100 | 1,818 | 50 |
| [ ] | `work/ruqyah_subcategories/ruqyah_subcategories_003.json` | 50 | 101-150 | 1,168 | 50 |
| [ ] | `work/ruqyah_subcategories/ruqyah_subcategories_004.json` | 13 | 151-163 | 138 | 13 |

## `ruqyah_videos`

Source: **BN** · fields: `name`, `author` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/ruqyah_videos/ruqyah_videos_001.json` | 50 | 1-50 | 2,511 | 50 |
| [ ] | `work/ruqyah_videos/ruqyah_videos_002.json` | 24 | 51-74 | 1,373 | 24 |

## `drawer_items`

Source: **BN** · fields: `title`, `hero_title1`, `hero_title2`, `content` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/drawer_items/drawer_items_001.json` | 3 | 19-21 | 4,512 | 4 |
| [ ] | `work/drawer_items/drawer_items_002.json` | 3 | 22-24 | 3,731 | 4 |

## `duas`

Source: **EN** · fields: `name`, `content`, `translation`, `note` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/duas/duas_001.json` | 15 | 1-15 | 5,906 | 15 |
| [ ] | `work/duas/duas_002.json` | 17 | 16-32 | 5,888 | 17 |
| [ ] | `work/duas/duas_003.json` | 18 | 33-50 | 5,759 | 18 |
| [ ] | `work/duas/duas_004.json` | 12 | 51-62 | 5,991 | 12 |
| [ ] | `work/duas/duas_005.json` | 14 | 63-76 | 5,636 | 14 |
| [ ] | `work/duas/duas_006.json` | 14 | 77-90 | 5,695 | 14 |
| [ ] | `work/duas/duas_007.json` | 10 | 91-100 | 5,649 | 10 |
| [ ] | `work/duas/duas_008.json` | 12 | 101-112 | 4,931 | 12 |
| [ ] | `work/duas/duas_009.json` | 8 | 113-120 | 5,951 | 8 |
| [ ] | `work/duas/duas_010.json` | 15 | 121-135 | 5,680 | 15 |
| [ ] | `work/duas/duas_011.json` | 8 | 136-143 | 5,496 | 8 |
| [ ] | `work/duas/duas_012.json` | 14 | 144-157 | 5,560 | 14 |
| [ ] | `work/duas/duas_013.json` | 14 | 158-171 | 5,800 | 14 |
| [ ] | `work/duas/duas_014.json` | 17 | 172-188 | 5,762 | 17 |
| [ ] | `work/duas/duas_015.json` | 16 | 189-204 | 5,632 | 16 |
| [ ] | `work/duas/duas_016.json` | 16 | 205-220 | 5,675 | 16 |
| [ ] | `work/duas/duas_017.json` | 14 | 221-234 | 5,780 | 14 |
| [ ] | `work/duas/duas_018.json` | 9 | 235-243 | 5,632 | 9 |
| [ ] | `work/duas/duas_019.json` | 12 | 244-255 | 5,939 | 12 |
| [ ] | `work/duas/duas_020.json` | 15 | 256-270 | 5,587 | 15 |
| [ ] | `work/duas/duas_021.json` | 8 | 271-278 | 5,361 | 8 |
| [ ] | `work/duas/duas_022.json` | 5 | 279-283 | 5,508 | 5 |
| [ ] | `work/duas/duas_023.json` | 14 | 284-297 | 5,838 | 14 |
| [ ] | `work/duas/duas_024.json` | 17 | 298-314 | 5,862 | 17 |
| [ ] | `work/duas/duas_025.json` | 13 | 315-327 | 5,833 | 13 |
| [ ] | `work/duas/duas_026.json` | 14 | 328-341 | 5,829 | 14 |
| [ ] | `work/duas/duas_027.json` | 19 | 342-360 | 5,840 | 19 |
| [ ] | `work/duas/duas_028.json` | 12 | 361-372 | 5,808 | 12 |
| [ ] | `work/duas/duas_029.json` | 18 | 373-390 | 5,880 | 18 |
| [ ] | `work/duas/duas_030.json` | 23 | 391-413 | 5,952 | 23 |
| [ ] | `work/duas/duas_031.json` | 12 | 414-425 | 5,791 | 12 |
| [ ] | `work/duas/duas_032.json` | 15 | 426-440 | 5,475 | 15 |
| [ ] | `work/duas/duas_033.json` | 19 | 441-459 | 5,800 | 19 |
| [ ] | `work/duas/duas_034.json` | 20 | 460-479 | 5,841 | 20 |
| [ ] | `work/duas/duas_035.json` | 15 | 480-494 | 5,646 | 15 |
| [ ] | `work/duas/duas_036.json` | 15 | 495-509 | 5,913 | 15 |
| [ ] | `work/duas/duas_037.json` | 15 | 510-524 | 5,270 | 15 |
| [ ] | `work/duas/duas_038.json` | 12 | 525-536 | 4,870 | 12 |
| [ ] | `work/duas/duas_039.json` | 12 | 537-548 | 5,602 | 12 |
| [ ] | `work/duas/duas_040.json` | 12 | 549-560 | 5,746 | 12 |
| [ ] | `work/duas/duas_041.json` | 9 | 561-569 | 5,681 | 9 |
| [ ] | `work/duas/duas_042.json` | 9 | 570-578 | 5,101 | 9 |
| [ ] | `work/duas/duas_043.json` | 12 | 579-590 | 5,568 | 12 |
| [ ] | `work/duas/duas_044.json` | 30 | 591-620 | 5,955 | 30 |
| [ ] | `work/duas/duas_045.json` | 35 | 621-655 | 5,956 | 35 |
| [ ] | `work/duas/duas_046.json` | 26 | 656-681 | 5,885 | 26 |
| [ ] | `work/duas/duas_047.json` | 24 | 682-705 | 5,943 | 24 |
| [ ] | `work/duas/duas_048.json` | 13 | 706-718 | 5,966 | 13 |
| [ ] | `work/duas/duas_049.json` | 9 | 719-727 | 5,974 | 9 |
| [ ] | `work/duas/duas_050.json` | 18 | 728-745 | 5,728 | 18 |
| [ ] | `work/duas/duas_051.json` | 12 | 746-757 | 5,280 | 12 |
| [ ] | `work/duas/duas_052.json` | 8 | 758-765 | 5,937 | 8 |
| [ ] | `work/duas/duas_053.json` | 10 | 766-775 | 5,875 | 10 |
| [ ] | `work/duas/duas_054.json` | 14 | 776-789 | 4,955 | 14 |
| [ ] | `work/duas/duas_055.json` | 8 | 790-797 | 5,892 | 8 |
| [ ] | `work/duas/duas_056.json` | 18 | 798-815 | 5,953 | 18 |
| [ ] | `work/duas/duas_057.json` | 17 | 816-832 | 5,654 | 17 |
| [ ] | `work/duas/duas_058.json` | 25 | 833-857 | 5,856 | 25 |
| [ ] | `work/duas/duas_059.json` | 27 | 858-884 | 5,887 | 27 |
| [ ] | `work/duas/duas_060.json` | 22 | 885-906 | 5,580 | 22 |
| [ ] | `work/duas/duas_061.json` | 25 | 907-931 | 5,728 | 25 |
| [ ] | `work/duas/duas_062.json` | 21 | 932-952 | 5,962 | 21 |
| [ ] | `work/duas/duas_063.json` | 27 | 953-979 | 5,957 | 27 |
| [ ] | `work/duas/duas_064.json` | 22 | 980-1001 | 3,194 | 22 |

## `ruqyah_instants`

Source: **EN** · fields: `topic_name`, `name`, `content`, `translation` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/ruqyah_instants/ruqyah_instants_001.json` | 18 | 1-18 | 5,463 | 18 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_002.json` | 14 | 19-32 | 5,222 | 14 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_003.json` | 8 | 33-40 | 4,922 | 8 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_004.json` | 12 | 41-52 | 5,396 | 12 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_005.json` | 17 | 53-69 | 5,786 | 17 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_006.json` | 19 | 70-88 | 5,941 | 19 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_007.json` | 16 | 89-104 | 5,723 | 16 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_008.json` | 21 | 105-125 | 5,791 | 21 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_009.json` | 18 | 126-143 | 5,982 | 18 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_010.json` | 14 | 144-157 | 5,580 | 14 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_011.json` | 16 | 158-173 | 5,835 | 16 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_012.json` | 16 | 174-189 | 5,735 | 16 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_013.json` | 11 | 190-200 | 5,565 | 11 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_014.json` | 11 | 201-211 | 5,633 | 11 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_015.json` | 4 | 212-215 | 5,918 | 4 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_016.json` | 8 | 216-223 | 5,720 | 8 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_017.json` | 21 | 224-244 | 5,946 | 21 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_018.json` | 24 | 245-268 | 5,777 | 24 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_019.json` | 22 | 269-290 | 5,866 | 22 |
| [ ] | `work/ruqyah_instants/ruqyah_instants_020.json` | 18 | 291-308 | 4,236 | 18 |

## `ruqyah_details`

Source: **EN** · fields: `topic_name`, `text` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/ruqyah_details/ruqyah_details_001.json` | 5 | 1-5 | 5,797 | 5 |
| [ ] | `work/ruqyah_details/ruqyah_details_002.json` | 2 | 6-7 | 1,715 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_003.json` | 1 | 8-8 | 4,682 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_004.json` | 1 | 9-9 | 4,856 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_005.json` | 2 | 9-10 | 4,697 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_006.json` | 1 | 11-11 | 4,713 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_007.json` | 4 | 12-15 | 5,973 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_008.json` | 2 | 16-17 | 2,805 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_009.json` | 1 | 18-18 | 4,409 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_010.json` | 1 | 19-19 | 4,207 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_011.json` | 3 | 20-22 | 3,925 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_012.json` | 2 | 23-24 | 4,685 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_013.json` | 2 | 25-26 | 4,367 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_014.json` | 1 | 26-26 | 4,963 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_015.json` | 1 | 26-26 | 4,889 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_016.json` | 1 | 26-26 | 5,011 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_017.json` | 2 | 26-27 | 4,280 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_018.json` | 2 | 28-29 | 4,484 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_019.json` | 1 | 30-30 | 5,691 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_020.json` | 2 | 30-31 | 5,777 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_021.json` | 2 | 32-33 | 5,215 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_022.json` | 2 | 34-35 | 5,764 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_023.json` | 3 | 36-38 | 3,508 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_024.json` | 1 | 39-39 | 5,534 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_025.json` | 2 | 40-41 | 5,424 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_026.json` | 2 | 42-43 | 5,850 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_027.json` | 3 | 44-46 | 5,933 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_028.json` | 3 | 47-49 | 5,995 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_029.json` | 1 | 50-50 | 4,230 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_030.json` | 2 | 51-52 | 5,995 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_031.json` | 1 | 53-53 | 1,857 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_032.json` | 1 | 54-54 | 4,712 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_033.json` | 2 | 55-56 | 4,271 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_034.json` | 2 | 57-58 | 4,487 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_035.json` | 2 | 59-60 | 5,864 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_036.json` | 2 | 61-62 | 4,370 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_037.json` | 3 | 63-65 | 5,867 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_038.json` | 1 | 66-66 | 5,751 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_039.json` | 5 | 66-70 | 5,642 | 5 |
| [ ] | `work/ruqyah_details/ruqyah_details_040.json` | 3 | 71-73 | 5,942 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_041.json` | 6 | 74-79 | 5,382 | 6 |
| [ ] | `work/ruqyah_details/ruqyah_details_042.json` | 8 | 80-87 | 5,486 | 8 |
| [ ] | `work/ruqyah_details/ruqyah_details_043.json` | 4 | 88-91 | 5,716 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_044.json` | 2 | 92-93 | 5,012 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_045.json` | 1 | 94-94 | 4,592 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_046.json` | 1 | 95-95 | 4,174 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_047.json` | 3 | 96-98 | 5,437 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_048.json` | 1 | 99-99 | 2,861 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_049.json` | 1 | 100-100 | 3,465 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_050.json` | 1 | 101-101 | 3,698 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_051.json` | 2 | 102-103 | 3,202 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_052.json` | 1 | 104-104 | 5,509 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_053.json` | 2 | 105-106 | 5,898 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_054.json` | 1 | 107-107 | 2,073 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_055.json` | 2 | 108-109 | 5,169 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_056.json` | 1 | 109-109 | 5,598 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_057.json` | 2 | 110-111 | 3,697 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_058.json` | 1 | 112-112 | 2,322 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_059.json` | 2 | 113-114 | 4,888 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_060.json` | 2 | 115-116 | 4,248 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_061.json` | 3 | 117-119 | 5,594 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_062.json` | 2 | 120-121 | 2,207 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_063.json` | 1 | 122-122 | 4,423 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_064.json` | 2 | 123-124 | 5,396 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_065.json` | 3 | 125-127 | 5,810 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_066.json` | 2 | 128-129 | 4,853 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_067.json` | 2 | 129-130 | 5,841 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_068.json` | 2 | 131-132 | 5,419 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_069.json` | 5 | 133-137 | 5,956 | 5 |
| [ ] | `work/ruqyah_details/ruqyah_details_070.json` | 4 | 138-141 | 5,329 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_071.json` | 6 | 142-147 | 5,638 | 6 |
| [ ] | `work/ruqyah_details/ruqyah_details_072.json` | 2 | 148-149 | 5,899 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_073.json` | 1 | 149-149 | 5,264 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_074.json` | 3 | 149-151 | 5,430 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_075.json` | 4 | 152-155 | 5,334 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_076.json` | 2 | 156-157 | 3,978 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_077.json` | 1 | 158-158 | 4,802 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_078.json` | 1 | 159-159 | 3,285 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_079.json` | 2 | 160-161 | 5,440 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_080.json` | 2 | 162-163 | 5,882 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_081.json` | 1 | 164-164 | 4,281 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_082.json` | 2 | 165-166 | 5,658 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_083.json` | 1 | 166-166 | 4,026 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_084.json` | 2 | 167-168 | 5,592 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_085.json` | 2 | 169-170 | 4,637 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_086.json` | 2 | 171-172 | 5,974 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_087.json` | 2 | 173-174 | 2,993 | 2 |
| [ ] | `work/ruqyah_details/ruqyah_details_088.json` | 1 | 175-175 | 5,734 | 1 |
| [ ] | `work/ruqyah_details/ruqyah_details_089.json` | 3 | 176-178 | 3,895 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_090.json` | 3 | 179-181 | 5,376 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_091.json` | 3 | 182-184 | 4,870 | 3 |
| [ ] | `work/ruqyah_details/ruqyah_details_092.json` | 5 | 185-189 | 5,314 | 5 |
| [ ] | `work/ruqyah_details/ruqyah_details_093.json` | 4 | 190-193 | 5,157 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_094.json` | 4 | 194-197 | 5,296 | 4 |
| [ ] | `work/ruqyah_details/ruqyah_details_095.json` | 3 | 198-200 | 4,604 | 3 |

## `dua_infos`

Source: **BN** · fields: `name`, `description` · key: `id`

| | File | Rows | IDs | Chars | Items |
|---|---|---:|---|---:|---:|
| [ ] | `work/dua_infos/dua_infos_001.json` | 2 | 1-2 | 5,764 | 4 |
| [ ] | `work/dua_infos/dua_infos_002.json` | 2 | 2-3 | 4,478 | 3 |
| [ ] | `work/dua_infos/dua_infos_003.json` | 1 | 3-3 | 5,444 | 3 |
| [ ] | `work/dua_infos/dua_infos_004.json` | 2 | 3-4 | 4,269 | 3 |
| [ ] | `work/dua_infos/dua_infos_005.json` | 1 | 4-4 | 5,104 | 3 |
| [ ] | `work/dua_infos/dua_infos_006.json` | 1 | 5-5 | 4,920 | 3 |
| [ ] | `work/dua_infos/dua_infos_007.json` | 1 | 5-5 | 5,952 | 4 |
| [ ] | `work/dua_infos/dua_infos_008.json` | 1 | 6-6 | 5,037 | 1 |
| [ ] | `work/dua_infos/dua_infos_009.json` | 1 | 7-7 | 5,050 | 3 |
| [ ] | `work/dua_infos/dua_infos_010.json` | 1 | 7-7 | 4,641 | 3 |
| [ ] | `work/dua_infos/dua_infos_011.json` | 1 | 8-8 | 5,735 | 3 |
| [ ] | `work/dua_infos/dua_infos_012.json` | 1 | 8-8 | 5,662 | 3 |
| [ ] | `work/dua_infos/dua_infos_013.json` | 1 | 8-8 | 5,740 | 3 |
| [ ] | `work/dua_infos/dua_infos_014.json` | 1 | 8-8 | 5,668 | 3 |
| [ ] | `work/dua_infos/dua_infos_015.json` | 1 | 8-8 | 5,152 | 3 |
| [ ] | `work/dua_infos/dua_infos_016.json` | 1 | 8-8 | 4,508 | 3 |
| [ ] | `work/dua_infos/dua_infos_017.json` | 1 | 9-9 | 5,315 | 3 |
| [ ] | `work/dua_infos/dua_infos_018.json` | 1 | 9-9 | 5,495 | 3 |
| [ ] | `work/dua_infos/dua_infos_019.json` | 1 | 9-9 | 5,164 | 3 |
| [ ] | `work/dua_infos/dua_infos_020.json` | 2 | 9-10 | 4,910 | 2 |
| [ ] | `work/dua_infos/dua_infos_021.json` | 2 | 11-12 | 5,623 | 3 |
| [ ] | `work/dua_infos/dua_infos_022.json` | 1 | 12-12 | 5,427 | 3 |
| [ ] | `work/dua_infos/dua_infos_023.json` | 2 | 13-14 | 5,951 | 2 |
| [ ] | `work/dua_infos/dua_infos_024.json` | 1 | 15-15 | 4,842 | 3 |
| [ ] | `work/dua_infos/dua_infos_025.json` | 1 | 15-15 | 5,405 | 4 |
| [ ] | `work/dua_infos/dua_infos_026.json` | 1 | 16-16 | 2,741 | 1 |
| [ ] | `work/dua_infos/dua_infos_027.json` | 1 | 17-17 | 4,939 | 1 |
| [ ] | `work/dua_infos/dua_infos_028.json` | 1 | 18-18 | 5,461 | 3 |
| [ ] | `work/dua_infos/dua_infos_029.json` | 1 | 18-18 | 5,533 | 3 |
| [ ] | `work/dua_infos/dua_infos_030.json` | 1 | 18-18 | 5,314 | 3 |
| [ ] | `work/dua_infos/dua_infos_031.json` | 2 | 18-19 | 4,993 | 2 |
| [ ] | `work/dua_infos/dua_infos_032.json` | 1 | 20-20 | 5,409 | 3 |
| [ ] | `work/dua_infos/dua_infos_033.json` | 1 | 20-20 | 5,179 | 4 |
| [ ] | `work/dua_infos/dua_infos_034.json` | 1 | 21-21 | 5,213 | 1 |
| [ ] | `work/dua_infos/dua_infos_035.json` | 2 | 22-23 | 5,492 | 2 |
| [ ] | `work/dua_infos/dua_infos_036.json` | 1 | 24-24 | 5,336 | 3 |
| [ ] | `work/dua_infos/dua_infos_037.json` | 2 | 24-25 | 5,364 | 3 |
| [ ] | `work/dua_infos/dua_infos_038.json` | 1 | 25-25 | 5,423 | 3 |
| [ ] | `work/dua_infos/dua_infos_039.json` | 1 | 25-25 | 2,134 | 2 |
| [ ] | `work/dua_infos/dua_infos_040.json` | 2 | 26-27 | 5,788 | 2 |
| [ ] | `work/dua_infos/dua_infos_041.json` | 1 | 27-27 | 5,431 | 3 |
| [ ] | `work/dua_infos/dua_infos_042.json` | 2 | 27-28 | 5,620 | 4 |
| [ ] | `work/dua_infos/dua_infos_043.json` | 1 | 28-28 | 4,610 | 3 |
| [ ] | `work/dua_infos/dua_infos_044.json` | 3 | 28-30 | 5,947 | 4 |
| [ ] | `work/dua_infos/dua_infos_045.json` | 2 | 31-32 | 4,763 | 2 |
| [ ] | `work/dua_infos/dua_infos_046.json` | 1 | 32-32 | 4,564 | 3 |
| [ ] | `work/dua_infos/dua_infos_047.json` | 1 | 32-32 | 4,873 | 3 |
| [ ] | `work/dua_infos/dua_infos_048.json` | 1 | 32-32 | 5,516 | 3 |
| [ ] | `work/dua_infos/dua_infos_049.json` | 2 | 32-33 | 5,972 | 4 |
| [ ] | `work/dua_infos/dua_infos_050.json` | 1 | 33-33 | 5,489 | 3 |
| [ ] | `work/dua_infos/dua_infos_051.json` | 1 | 33-33 | 5,644 | 3 |
| [ ] | `work/dua_infos/dua_infos_052.json` | 1 | 33-33 | 4,741 | 3 |
| [ ] | `work/dua_infos/dua_infos_053.json` | 1 | 33-33 | 4,883 | 3 |
| [ ] | `work/dua_infos/dua_infos_054.json` | 1 | 33-33 | 5,455 | 3 |
| [ ] | `work/dua_infos/dua_infos_055.json` | 2 | 33-34 | 5,805 | 4 |
| [ ] | `work/dua_infos/dua_infos_056.json` | 1 | 34-34 | 5,455 | 3 |
| [ ] | `work/dua_infos/dua_infos_057.json` | 2 | 34-35 | 5,547 | 4 |
| [ ] | `work/dua_infos/dua_infos_058.json` | 1 | 35-35 | 4,695 | 3 |
| [ ] | `work/dua_infos/dua_infos_059.json` | 1 | 35-35 | 5,053 | 3 |
| [ ] | `work/dua_infos/dua_infos_060.json` | 1 | 35-35 | 5,535 | 3 |
| [ ] | `work/dua_infos/dua_infos_061.json` | 1 | 35-35 | 5,748 | 3 |
| [ ] | `work/dua_infos/dua_infos_062.json` | 2 | 35-36 | 5,049 | 3 |
| [ ] | `work/dua_infos/dua_infos_063.json` | 1 | 37-37 | 5,670 | 3 |
| [ ] | `work/dua_infos/dua_infos_064.json` | 1 | 37-37 | 4,704 | 3 |
| [ ] | `work/dua_infos/dua_infos_065.json` | 1 | 37-37 | 2,549 | 2 |
| [ ] | `work/dua_infos/dua_infos_066.json` | 1 | 38-38 | 5,474 | 1 |
| [ ] | `work/dua_infos/dua_infos_067.json` | 1 | 39-39 | 3,459 | 1 |
| [ ] | `work/dua_infos/dua_infos_068.json` | 1 | 40-40 | 4,764 | 1 |
| [ ] | `work/dua_infos/dua_infos_069.json` | 2 | 41-42 | 5,331 | 3 |
| [ ] | `work/dua_infos/dua_infos_070.json` | 1 | 42-42 | 3,103 | 2 |

