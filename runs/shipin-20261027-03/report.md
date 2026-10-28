# 铁勺 生成报告

slug：`shipin-20261027-03`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5923
LLM 调用：57 次，累计 129.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁勺撞翻油锅 | 662 | short | 95.1 | 0 |  | 0 |
| 2 | 手机屏幕贴住木板 | 1130 | normal | 92.7 | 0 |  | 1 |
| 3 | 钥匙划亮黑暗 | 1098 | normal | 36.6 | 0 |  | 2 |
| 4 | 铁勺划地计数 | 1150 | normal | 94.4 | 0 |  | 0 |
| 5 | 二维码撕落瞬间 | 1016 | normal | 93.3 | 0 |  | 0 |
| 6 | 米粒坠入尘埃 | 861 | normal | 36.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「李阿婆的」×3
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「你们再吵下去，我就关上门了…」）
- 第 6 章：
  - [observe] 章节过短 765 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5500
chapter_chars_mean: 917
chapter_chars_median: 996
chapter_chars_cv: 0.21
paragraphs_mean: 27.5
dialogue_chars_pct: 23.2
dialogue_para_pct: 49.2
interiority_para_pct: 0.0
narration_para_pct: 50.8
turn_under20_pct: 93.7
turn_over200_pct: 0.0
attr_say_pct: 37.6
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.1
turn_len_median: 12
```
