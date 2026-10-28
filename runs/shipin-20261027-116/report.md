# 旧票 生成报告

slug：`shipin-20261027-116`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6756
LLM 调用：57 次，累计 144.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸片压入抽屉 | 456 | short | 38.8 | 0 |  | 1 |
| 2 | 纸片上的裂痕 | 1373 | normal | 36.5 | 0 |  | 2 |
| 3 | 扫帚拂过木箱 | 1056 | normal | 36.8 | 0 |  | 1 |
| 4 | 纸片压入铁皮柜 | 1283 | normal | 34.4 | 0 |  | 5 |
| 5 | 纸片贴胸的瞬间 | 1411 | normal | 55.4 | 0 |  | 0 |
| 6 | 手电筒照红纸片 | 1171 | normal | 86.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 420 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「纸片在他掌中皱成一团，露出一角蓝色的布料——那是…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这箱子已经三天没动过了…」）
- 第 4 章：
  - 单条套路句式超限：「陈建国的」×3
  - narration_para_pct 17.2 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
  - [observe] 章内自我复读 5 句（如「你父亲最后一次坐渡轮，就是用这张票…」）
  - [observe] 标题与《纸片压入抽屉》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - interiority_para_pct 7.7 高于目标 6.0
  - narration_para_pct 34.6 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6321
chapter_chars_mean: 1054
chapter_chars_median: 1157
chapter_chars_cv: 0.32
paragraphs_mean: 28.5
dialogue_chars_pct: 24.0
dialogue_para_pct: 59.3
interiority_para_pct: 2.5
narration_para_pct: 38.2
turn_under20_pct: 94.3
turn_over200_pct: 0.0
attr_say_pct: 75.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 9
```
