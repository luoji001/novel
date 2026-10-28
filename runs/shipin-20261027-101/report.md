# 二维码 生成报告

slug：`shipin-20261027-101`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5849
LLM 调用：57 次，累计 133.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴纸边缘的颤动 | 388 | short | 22.4 | 0 |  | 1 |
| 2 | 铁皮锅的重逢 | 1072 | normal | 93.1 | 0 |  | 1 |
| 3 | 塑料袋裂开的瞬间 | 876 | normal | 38.6 | 0 |  | 1 |
| 4 | 粉条触地的刹那 | 1338 | normal | 36.3 | 0 |  | 1 |
| 5 | 二维码贴纸的争夺 | 1370 | normal | 36.4 | 0 |  | 2 |
| 6 | 二维码贴纸的争夺 | 799 | normal | 37.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 347 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 3 章：
  - [observe] 章节过短 804 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「你要是怕麻烦，可以去隔壁王婶那借个板凳…」）
- 第 5 章：
  - 单条套路句式超限：「李阿婆的」×3
  - [observe] 章内自我复读 4 句（如「因为我看到了你每天做些什么…」）
- 第 6 章：
  - [observe] 章节过短 749 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「二维码贴纸的争夺」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5421
chapter_chars_mean: 904
chapter_chars_median: 905
chapter_chars_cv: 0.38
paragraphs_mean: 27.5
dialogue_chars_pct: 22.5
dialogue_para_pct: 55.7
interiority_para_pct: 0.0
narration_para_pct: 44.3
turn_under20_pct: 91.3
turn_over200_pct: 0.0
attr_say_pct: 26.8
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.9
turn_len_median: 10
```
