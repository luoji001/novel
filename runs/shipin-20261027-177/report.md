# 录像带 生成报告

slug：`shipin-20261027-177`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7755
LLM 调用：57 次，累计 141.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控录像带的重量 | 766 | short | 95.2 | 0 |  | 0 |
| 2 | 铜钥匙撬开的裂缝 | 1189 | normal | 93.6 | 0 |  | 0 |
| 3 | 薄荷糖的余味 | 1332 | normal | 95.5 | 0 |  | 3 |
| 4 | 门禁卡与电线交锋 | 1159 | normal | 92.4 | 0 |  | 1 |
| 5 | 门禁卡的最后一步 | 1906 | normal | 92.8 | 0 |  | 0 |
| 6 | 擦拭铜钥匙的红围巾 | 1397 | normal | 35.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - narration_para_pct 20.8 低于目标 35.0
  - attr_adv_pct 12.5 高于目标 10.0
  - dialogue_run_mean 4.6 高于目标 4.0
- 第 4 章：
  - 命中套话收尾句
- 第 6 章：
  - interiority_para_pct 8.0 高于目标 6.0
  - [observe] 章内自我复读 2 句（如「我儿子丢了之前，家里那只猫总是半夜跑出去。后来它…」）

## 整书结构指标

```
chapters: 6
total_chars: 7140
chapter_chars_mean: 1190
chapter_chars_median: 1168
chapter_chars_cv: 0.27
paragraphs_mean: 39.2
dialogue_chars_pct: 28.6
dialogue_para_pct: 56.8
interiority_para_pct: 2.3
narration_para_pct: 41.0
turn_under20_pct: 87.9
turn_over200_pct: 0.0
attr_say_pct: 69.6
attr_adv_pct: 2.1
scenes_per_chapter: 2.5
dialogue_run_mean: 2.6
turn_len_median: 10
```
