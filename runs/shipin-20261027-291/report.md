# 铜钥匙 生成报告

slug：`shipin-20261027-291`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6924
LLM 调用：57 次，累计 138.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴标签纸 | 786 | short | 95.4 | 0 |  | 0 |
| 2 | 电话线缠绕手腕 | 1138 | normal | 21.3 | 0 |  | 2 |
| 3 | 胶片盒的标签纸 | 1312 | normal | 36.7 | 0 |  | 1 |
| 4 | 胶片缓缓入槽 | 1385 | normal | 89.5 | 0 |  | 0 |
| 5 | 贴标签纸 | 1207 | normal | 91.2 | 0 |  | 1 |
| 6 | 钥匙与照片的重量 | 1090 | normal | 59.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「小林，把老周那份档案调出来…」）
- 第 3 章：
  - [observe] attr_adv_pct 28.6 > 18.0（结构塌缩）
- 第 5 章：
  - [observe] 标题重复：「贴标签纸」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6422
chapter_chars_mean: 1070
chapter_chars_median: 1090
chapter_chars_cv: 0.19
paragraphs_mean: 34.3
dialogue_chars_pct: 17.9
dialogue_para_pct: 39.2
interiority_para_pct: 1.0
narration_para_pct: 59.9
turn_under20_pct: 94.9
turn_over200_pct: 0.0
attr_say_pct: 55.0
attr_adv_pct: 8.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.3
turn_len_median: 10
```
