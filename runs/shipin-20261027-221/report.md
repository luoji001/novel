# 胶片盒 生成报告

slug：`shipin-20261027-221`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6958
LLM 调用：57 次，累计 137.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭镜头盖 | 479 | short | 21.5 | 0 |  | 2 |
| 2 | 公文包坠落瞬间 | 1259 | normal | 37.8 | 0 |  | 1 |
| 3 | 胶片盒被握紧 | 1397 | normal | 86.2 | 0 |  | 2 |
| 4 | 胶片盒被轻轻擦亮 | 1303 | normal | 53.5 | 0 |  | 0 |
| 5 | 钥匙划过玻璃碴 | 1178 | normal | 36.7 | 0 |  | 2 |
| 6 | 胶片盒被紧紧攥住 | 1336 | normal | 87.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.3 低于目标 5.0
  - [observe] 章节过短 450 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「老李站在」×3
  - interiority_para_pct 8.8 高于目标 6.0
- 第 5 章：
  - 单条套路句式超限：「陈镇长的」×3
  - [observe] 章内自我复读 3 句（如「昨天还看见小梅站在门口卖票，她说今天有人来找她，…」）
- 第 6 章：
  - [observe] 标题与《胶片盒被握紧》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6546
chapter_chars_mean: 1091
chapter_chars_median: 1202
chapter_chars_cv: 0.29
paragraphs_mean: 26.3
dialogue_chars_pct: 23.1
dialogue_para_pct: 49.1
interiority_para_pct: 2.3
narration_para_pct: 48.5
turn_under20_pct: 87.1
turn_over200_pct: 0.0
attr_say_pct: 22.0
attr_adv_pct: 4.8
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
