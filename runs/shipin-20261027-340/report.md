# 泛黄的船票 生成报告

slug：`shipin-20261027-340`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6131
LLM 调用：57 次，累计 132.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸面的手指 | 625 | short | 39.9 | 0 |  | 1 |
| 2 | 手机贴额头的蓝光 | 1246 | normal | 90.8 | 0 |  | 1 |
| 3 | 钥匙坠入锁孔的刹那 | 1005 | normal | 92.6 | 0 |  | 0 |
| 4 | 手指抚过船票边缘 | 1054 | normal | 90.9 | 0 |  | 0 |
| 5 | 船票与青龙纹身 | 1102 | normal | 34.3 | 0 |  | 3 |
| 6 | 船票与青龙纹身 | 1093 | normal | 90.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 568 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 30.4 低于目标 35.0
- 第 5 章：
  - narration_para_pct 12.0 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0
  - [observe] 章内自我复读 6 句（如「这是他的东西，不该再有人拥有…」）
- 第 6 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 标题重复：「船票与青龙纹身」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5721
chapter_chars_mean: 954
chapter_chars_median: 1001
chapter_chars_cv: 0.22
paragraphs_mean: 25.8
dialogue_chars_pct: 26.0
dialogue_para_pct: 65.4
interiority_para_pct: 1.3
narration_para_pct: 33.3
turn_under20_pct: 94.4
turn_over200_pct: 0.0
attr_say_pct: 32.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.9
turn_len_median: 8
```
