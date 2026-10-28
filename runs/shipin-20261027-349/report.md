# 扫码箱 生成报告

slug：`shipin-20261027-349`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6773
LLM 调用：57 次，累计 141.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与红光较量 | 554 | short | 37.7 | 0 |  | 1 |
| 2 | 钥匙与红光较量 | 1340 | normal | 89.9 | 0 |  | 2 |
| 3 | 红光下的交易 | 1190 | normal | 92.5 | 0 |  | 1 |
| 4 | 皮箱与红光对峙 | 1187 | normal | 90.6 | 0 |  | 1 |
| 5 | 红光下的钥匙较量 | 1388 | normal | 89.4 | 0 |  | 4 |
| 6 | 皮箱与蓝光对峙 | 1108 | normal | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 505 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「李正阳的」×4
  - [observe] 标题重复：「钥匙与红光较量」已存在
- 第 3 章：
  - 单条套路句式超限：「赵子安的」×6
- 第 4 章：
  - 单条套路句式超限：「赵子安的」×3、「李正阳的」×3
- 第 5 章：
  - 单条套路句式超限：「李正阳站在」×3
  - 情节与已写章节重复 0.64 ≥ 0.62（撞上「李正阳与赵子安争夺装有军方加密容器的皮箱，双方在充电桩旁…」）
  - narration_para_pct 29.7 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 6 章：
  - [observe] 标题与《皮箱与红光对峙》近似 0.86 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6271
chapter_chars_mean: 1045
chapter_chars_median: 1118
chapter_chars_cv: 0.27
paragraphs_mean: 31.7
dialogue_chars_pct: 21.3
dialogue_para_pct: 52.6
interiority_para_pct: 0.5
narration_para_pct: 47.0
turn_under20_pct: 97.3
turn_over200_pct: 0.0
attr_say_pct: 29.1
attr_adv_pct: 2.9
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
