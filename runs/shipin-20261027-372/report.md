# 信封 生成报告

slug：`shipin-20261027-372`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7322
LLM 调用：57 次，累计 156.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 信封在冰面飘荡 | 670 | short | 45.8 | 0 |  | 2 |
| 2 | 鱼鳞与冰台较量 | 1429 | normal | 35.6 | 0 |  | 1 |
| 3 | 鱼鳞争夺战 | 1361 | normal | 59.8 | 0 |  | 0 |
| 4 | 竹竿与塑料袋较量 | 1440 | normal | 91.3 | 0 |  | 1 |
| 5 | 鱼鳞与哨子对决 | 1099 | normal | 92.8 | 0 |  | 1 |
| 6 | 鱼鳞与信封争夺 | 1317 | normal | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.0 低于目标 5.0
  - narration_para_pct 96.6 高于目标 90.0
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「你要是敢动，我就把这鱼鳞扔进水里…」）
- 第 4 章：
  - narration_para_pct 32.4 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「李大柱的」×4
- 第 6 章：
  - [observe] 标题与《鱼鳞争夺战》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6819
chapter_chars_mean: 1136
chapter_chars_median: 1266
chapter_chars_cv: 0.26
paragraphs_mean: 34
dialogue_chars_pct: 12.8
dialogue_para_pct: 40.0
interiority_para_pct: 1.2
narration_para_pct: 58.7
turn_under20_pct: 99.2
turn_over200_pct: 0.0
attr_say_pct: 18.3
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.6
turn_len_median: 7
```
