# 铁钳与报纸 生成报告

slug：`shipin-20261027-397`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7054
LLM 调用：57 次，累计 143.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁钳卡门瞬间 | 675 | short | 95.4 | 0 |  | 0 |
| 2 | 报纸覆盖的台阶 | 1277 | normal | 38.2 | 0 |  | 1 |
| 3 | 铁钳与雨靴之争 | 1249 | normal | 92.4 | 0 |  | 0 |
| 4 | 报纸覆盖的台阶 | 1360 | normal | 92.9 | 0 |  | 1 |
| 5 | 铁钳抵住电梯门 | 1340 | normal | 93.6 | 0 |  | 1 |
| 6 | 铁钳抵住电梯门 | 1147 | normal | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「张叔的手指收紧了些，报纸边缘开始卷起一丝丝毛边…」）
- 第 4 章：
  - [observe] 标题重复：「报纸覆盖的台阶」已存在
- 第 5 章：
  - attr_adv_pct 12.5 高于目标 10.0
- 第 6 章：
  - [observe] 标题重复：「铁钳抵住电梯门」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6651
chapter_chars_mean: 1108
chapter_chars_median: 1183
chapter_chars_cv: 0.22
paragraphs_mean: 25.7
dialogue_chars_pct: 24.2
dialogue_para_pct: 56.6
interiority_para_pct: 0.0
narration_para_pct: 43.4
turn_under20_pct: 92.4
turn_over200_pct: 0.0
attr_say_pct: 42.8
attr_adv_pct: 2.3
scenes_per_chapter: 1.3
dialogue_run_mean: 2.3
turn_len_median: 10
```
