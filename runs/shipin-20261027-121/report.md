# 锁屏 生成报告

slug：`shipin-20261027-121`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6383
LLM 调用：57 次，累计 129.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏上的黑影 | 431 | short | 35.9 | 0 |  | 3 |
| 2 | 指纹与裂痕 | 782 | normal | 36.3 | 0 |  | 1 |
| 3 | 钥匙里的异物 | 1234 | normal | 91.1 | 0 |  | 1 |
| 4 | 钥匙缝进轮胎纹路 | 1450 | normal | 87.7 | 0 |  | 2 |
| 5 | 钥匙缝进轮胎纹路 | 1565 | normal | 92.4 | 0 |  | 2 |
| 6 | 数字消失的瞬间 | 915 | normal | 34.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.1 低于目标 5.0
  - interiority_para_pct 8.3 高于目标 6.0
  - [observe] 章节过短 392 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 721 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「小林站在」×3
- 第 4 章：
  - 单条套路句式超限：「小林站在」×3
  - interiority_para_pct 7.4 高于目标 6.0
- 第 5 章：
  - 单条套路句式超限：「小林站在」×3
  - [observe] 标题重复：「钥匙缝进轮胎纹路」已存在
- 第 6 章：
  - narration_para_pct 94.4 高于目标 90.0
  - [observe] 章内自我复读 10 句（如「翻开其中一页，上面写着“12月1日…」）
  - [observe] 章节过短 705 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5823
chapter_chars_mean: 970
chapter_chars_median: 932
chapter_chars_cv: 0.44
paragraphs_mean: 32.8
dialogue_chars_pct: 9.8
dialogue_para_pct: 30.6
interiority_para_pct: 3.7
narration_para_pct: 65.7
turn_under20_pct: 94.4
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 1.2
turn_len_median: 8
```
