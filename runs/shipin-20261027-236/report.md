# 硬币的归属 生成报告

slug：`shipin-20261027-236`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6892
LLM 调用：57 次，累计 132.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币坠入裤袋 | 309 | short | 34.2 | 0 |  | 3 |
| 2 | 纸条上的感谢 | 1598 | normal | 91.7 | 0 |  | 2 |
| 3 | 硬币卡进方向盘缝隙 | 1346 | normal | 91.8 | 0 |  | 0 |
| 4 | 钥匙的归处 | 1139 | normal | 94.3 | 0 |  | 0 |
| 5 | 硬币铺成星河 | 1089 | normal | 36.2 | 0 |  | 3 |
| 6 | 硬币与红绳的对峙 | 1405 | normal | 88.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 267 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 34.5 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 4.3 低于目标 5.0
  - narration_para_pct 94.2 高于目标 90.0
  - [observe] 章内自我复读 5 句（如「陈志强低头看向铁盒表面刻着的号码…」）

## 整书结构指标

```
chapters: 6
total_chars: 6364
chapter_chars_mean: 1061
chapter_chars_median: 1162
chapter_chars_cv: 0.41
paragraphs_mean: 32
dialogue_chars_pct: 18.2
dialogue_para_pct: 48.3
interiority_para_pct: 1.4
narration_para_pct: 50.3
turn_under20_pct: 95.5
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.2
turn_len_median: 10
```
