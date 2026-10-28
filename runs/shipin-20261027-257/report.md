# 雨靴的裂痕 生成报告

slug：`shipin-20261027-257`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6500
LLM 调用：57 次，累计 135.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 花生袋的重量 | 478 | short | 23.8 | 0 |  | 3 |
| 2 | 铁锹与门框的较量 | 1166 | normal | 96.0 | 0 |  | 1 |
| 3 | 踩靴之争 | 1285 | normal | 94.3 | 0 |  | 0 |
| 4 | 猫爪与铁锹 | 1168 | normal | 90.6 | 0 |  | 0 |
| 5 | 花生落地的瞬间 | 1186 | normal | 37.4 | 0 |  | 1 |
| 6 | 手电筒照见刻痕 | 1211 | normal | 91.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

1. 第一章提到“李阿姨”，但后续章节中未再出现“李阿姨”这一称呼，仅出现“周建国”“林小满”“陈桂花”等人物，存在人物称呼不一致的问题。

2. 第五章提到“张大爷”，但前文未出现“张大爷”这一人物，属于人物出场不一致。

3. 第六章提到“鞋底刻有彼此名字”，但前文未提及任何关于鞋底刻字的伏笔或铺垫，属于物件交代缺失。

4. 第四章提到“房产归属真相”，但前文未明确提及房产归属问题，属于情节铺垫不足。

5. 第三章提到“周建国为保护自己的房产证”，但前文未提及“房产证”这一物件，属于物件出现无铺垫。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 444 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 29.6 低于目标 35.0
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「林小满低头看着地板上散落的花生粒，它们静静躺在那…」）

## 整书结构指标

```
chapters: 6
total_chars: 6063
chapter_chars_mean: 1010
chapter_chars_median: 1104
chapter_chars_cv: 0.28
paragraphs_mean: 28.7
dialogue_chars_pct: 20.2
dialogue_para_pct: 52.1
interiority_para_pct: 0.7
narration_para_pct: 47.2
turn_under20_pct: 96.3
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.4
turn_len_median: 9
```
