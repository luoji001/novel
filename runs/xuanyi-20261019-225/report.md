# 空钥 生成报告

slug：`xuanyi-20261019-225`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14675
LLM 调用：68 次，累计 229.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 录像带上的空缺片段 | 2181 | short | 82.4 | 0 |  | 3 |
| 2 | 打印机纸张上的神秘标记 | 3675 | normal | 48.6 | 0 |  | 4 |
| 3 | 处方单背面的指纹痕迹 | 3520 | normal | 50.7 | 0 |  | 1 |
| 4 | 钥匙在掌心发烫 | 3403 | normal | 88.9 | 0 |  | 3 |
| 5 | 夜班记录本被反复翻阅 | 1891 | short | 77.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林秋实的」×3
  - dialogue_chars_pct 11.6 低于目标 20.0
  - interiority_para_pct 22.6 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 12.8 低于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 1 句（如「夜风吹过玻璃窗，在墙上投下斑驳的影子…」）
- 第 3 章：
  - dialogue_chars_pct 13.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林秋实的」×9、「变得更加」×3
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他回头看向监控屏幕，里面依旧显示出正常的画面——…」）
- 第 5 章：
  - 单条套路句式超限：「他知道自己」×4、「林秋实的」×3
  - dialogue_chars_pct 12.8 低于目标 20.0
  - interiority_para_pct 25.0 高于目标 20.0
  - narration_para_pct 14.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14029
chapter_chars_mean: 2806
chapter_chars_median: 3220
chapter_chars_cv: 0.28
paragraphs_mean: 55.4
dialogue_chars_pct: 16.9
dialogue_para_pct: 52.5
interiority_para_pct: 17.7
narration_para_pct: 29.7
turn_under20_pct: 87.8
turn_over200_pct: 0.0
attr_say_pct: 27.3
attr_adv_pct: 4.2
scenes_per_chapter: 2.6
dialogue_run_mean: 2.0
turn_len_median: 10
```
