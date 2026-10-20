# 水表 生成报告

slug：`xuanyi-20261019-148`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15331
LLM 调用：68 次，累计 228.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表内部的孔洞 | 1591 | short | 80.4 | 0 |  | 2 |
| 2 | 钥匙开启沉寂之门 | 4730 | normal | 82.0 | 0 |  | 3 |
| 3 | 身份证揭开真相 | 3235 | normal | 90.1 | 0 |  | 2 |
| 4 | 打开旧箱子的瞬间 | 3473 | normal | 87.2 | 0 |  | 3 |
| 5 | 拧动水表螺丝的瞬间 | 2297 | short | 88.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 10.3 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「林永年的」×4
  - dialogue_chars_pct 15.3 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「毕竟对于这样一个看似普通的家庭琐事而言，背后却似…」）
- 第 3 章：
  - narration_para_pct 12.0 低于目标 20.0
  - [observe] 章内自我复读 8 句（如「老张没有回答他的问题，而是缓缓地翻开身份证背面，…」）
- 第 4 章：
  - 单条套路句式超限：「他知道自己」×3、「林永年的」×3
  - narration_para_pct 16.2 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「林永年环顾四周，压低声音道：“我调查过了，这栋楼…」）
- 第 5 章：
  - 单条套路句式超限：「林永年的」×4
  - narration_para_pct 17.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14666
chapter_chars_mean: 2933
chapter_chars_median: 3070
chapter_chars_cv: 0.4
paragraphs_mean: 58
dialogue_chars_pct: 24.0
dialogue_para_pct: 62.0
interiority_para_pct: 14.3
narration_para_pct: 23.6
turn_under20_pct: 80.9
turn_over200_pct: 0.0
attr_say_pct: 15.2
attr_adv_pct: 1.3
scenes_per_chapter: 4
dialogue_run_mean: 3.0
turn_len_median: 12
```
