# 酱油罐 生成报告

slug：`shipin-20261027-51`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6654
LLM 调用：57 次，累计 144.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 车顶人影窥视便利店 | 309 | short | 11.8 | 0 |  | 3 |
| 2 | 敲击铁皮罐子 | 1492 | normal | 94.0 | 0 |  | 4 |
| 3 | 钥匙与铁皮罐子对峙 | 1391 | normal | 88.2 | 0 |  | 2 |
| 4 | 酱油瓶底的纸条 | 1154 | normal | 92.0 | 0 |  | 0 |
| 5 | 红色丝巾的传递 | 1231 | normal | 88.6 | 0 |  | 2 |
| 6 | 钥匙转动的瞬间 | 1071 | normal | 23.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 264 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×6
  - interiority_para_pct 7.0 高于目标 6.0
  - narration_para_pct 18.6 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 3 章：
  - 情节与已写章节重复 0.67 ≥ 0.62（撞上「小林在便利店遇到神秘男子陈志远，对方声称要找回父亲留下的…」）
  - interiority_para_pct 8.8 高于目标 6.0
- 第 5 章：
  - 单条套路句式超限：「小林站在」×3
  - interiority_para_pct 7.7 高于目标 6.0
- 第 6 章：
  - 单条套路句式超限：「小林站在」×3
  - [observe] 章内自我复读 3 句（如「他伸手将门完全推上，指尖触碰到冰冷的金属表面，感…」）

## 整书结构指标

```
chapters: 6
total_chars: 6101
chapter_chars_mean: 1017
chapter_chars_median: 1098
chapter_chars_cv: 0.4
paragraphs_mean: 33
dialogue_chars_pct: 20.2
dialogue_para_pct: 44.6
interiority_para_pct: 5.8
narration_para_pct: 49.6
turn_under20_pct: 93.8
turn_over200_pct: 0.0
attr_say_pct: 29.1
attr_adv_pct: 3.4
scenes_per_chapter: 2.3
dialogue_run_mean: 2.0
turn_len_median: 10
```
