# 铜钥 生成报告

slug：`shipin-20261027-290`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5920
LLM 调用：57 次，累计 124.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙落进晨光 | 292 | short | 18.5 | 0 |  | 3 |
| 2 | 贝壳落入晨光 | 1081 | normal | 37.2 | 0 |  | 1 |
| 3 | 镇纸压住页脚 | 1042 | normal | 51.8 | 0 |  | 0 |
| 4 | 钥匙贴近收音机 | 995 | normal | 91.5 | 0 |  | 0 |
| 5 | 钥匙划过玻璃罐 | 1328 | normal | 90.2 | 0 |  | 3 |
| 6 | 铜铃铛轻响 | 1176 | normal | 93.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 254 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 3 句（如「他的影子被阳光拉得很长，斜斜地铺在地上，与墙上的…」）
- 第 5 章：
  - 单条套路句式超限：「林晚晴的」×3
  - narration_para_pct 15.6 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
- 第 6 章：
  - 单条套路句式超限：「沈怀远的」×4

## 整书结构指标

```
chapters: 6
total_chars: 5545
chapter_chars_mean: 924
chapter_chars_median: 1002
chapter_chars_cv: 0.37
paragraphs_mean: 22.5
dialogue_chars_pct: 20.4
dialogue_para_pct: 53.3
interiority_para_pct: 1.5
narration_para_pct: 45.2
turn_under20_pct: 97.4
turn_over200_pct: 0.0
attr_say_pct: 50.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.5
turn_len_median: 10
```
