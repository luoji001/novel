# 钥匙 生成报告

slug：`xuanyi-20261019-04`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14464
LLM 调用：68 次，累计 236.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的陌生名字 | 1687 | short | 96.7 | 0 |  | 0 |
| 2 | 锈蚀的钥匙 | 3507 | normal | 92.8 | 0 |  | 4 |
| 3 | 锈蚀的铁皮柜 | 3659 | normal | 90.4 | 0 |  | 2 |
| 4 | 照片背面的碎纸片 | 3861 | normal | 89.7 | 0 |  | 2 |
| 5 | 摩挲泛黄纸页 | 1745 | short | 91.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈国栋的」×7、「周淑芬的」×5、「周淑芬点」×4
  - narration_para_pct 8.1 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「陈国栋的声音低沉了一些…」）
- 第 3 章：
  - 单条套路句式超限：「陈国栋的」×10、「周淑芬的」×7、「“我不知道」×3
  - narration_para_pct 18.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈国栋的」×10、「周淑芬的」×4、「为什么会」×4
  - attr_adv_pct 16.7 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「陈国栋的」×4、「周淑芬的」×3
  - narration_para_pct 18.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13803
chapter_chars_mean: 2761
chapter_chars_median: 3346
chapter_chars_cv: 0.38
paragraphs_mean: 58.4
dialogue_chars_pct: 32.9
dialogue_para_pct: 71.8
interiority_para_pct: 10.5
narration_para_pct: 17.7
turn_under20_pct: 78.8
turn_over200_pct: 0.0
attr_say_pct: 21.9
attr_adv_pct: 9.0
scenes_per_chapter: 2.4
dialogue_run_mean: 3.8
turn_len_median: 12
```
