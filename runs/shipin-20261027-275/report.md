# 屏角 生成报告

slug：`shipin-20261027-275`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5743
LLM 调用：57 次，累计 118.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕的温度 | 621 | short | 38.0 | 0 |  | 1 |
| 2 | 钥匙坠入车缝 | 1185 | normal | 93.0 | 0 |  | 0 |
| 3 | 纸币滑落的轨迹 | 650 | normal | 22.3 | 0 |  | 3 |
| 4 | 钥匙与暗红印记 | 1020 | normal | 90.8 | 0 |  | 0 |
| 5 | 钥匙触及收银机 | 1209 | normal | 58.3 | 0 |  | 2 |
| 6 | 触摸屏幕的裂痕 | 1052 | normal | 34.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到陈默“试图占据监控屏幕位置”，但第六章提到小林“发现神秘身影”在监控中，暗示监控屏幕位置被调整，但未明确说明是陈默调整，存在人物行为与结果的关联不明确。

2. 第三章提到“纸币上的时间与灯光闪烁同步”，但未提及任何关于灯光闪烁的具体描写或前文铺垫，属于物件出现无前因。

3. 第五章提到陈默“用钥匙打开门锁”，但第二章提到陈默“试图占据监控屏幕位置”，两者行为逻辑不一致，钥匙与监控屏幕位置无直接关联，存在行为动机不清晰。

4. 第六章提到“液体痕迹与屏幕异常”，但前文未提及任何液体或屏幕异常的铺垫，属于新出现的元素无前因。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 546 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 512 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 6 章：
  - dialogue_chars_pct 3.4 低于目标 5.0
  - [observe] 章内自我复读 4 句（如「液体有些粘稠，在冷光灯下泛出微弱的光泽…」）

## 整书结构指标

```
chapters: 6
total_chars: 5227
chapter_chars_mean: 871
chapter_chars_median: 943
chapter_chars_cv: 0.32
paragraphs_mean: 32
dialogue_chars_pct: 8.1
dialogue_para_pct: 22.6
interiority_para_pct: 0.8
narration_para_pct: 76.6
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 18.1
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.4
turn_len_median: 9
```
