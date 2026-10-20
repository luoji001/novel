# 行李箱 生成报告

slug：`xuanyi-20261019-63`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15565
LLM 调用：68 次，累计 250.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行李箱重现 | 1944 | short | 100.0 | 0 |  | 2 |
| 2 | 钥匙与消毒水味 | 4193 | normal | 89.0 | 0 |  | 4 |
| 3 | 纸条的日期 | 3629 | normal | 91.6 | 0 |  | 3 |
| 4 | 钥匙与纸条对话 | 3830 | normal | 88.6 | 0 |  | 4 |
| 5 | 木板下的秘密 | 1964 | short | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”林婉儿轻」×3、「林婉儿点」×3
  - narration_para_pct 14.8 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林婉儿的」×4、「“我不知道」×3、「带着一丝」×3
  - narration_para_pct 16.8 低于目标 20.0
  - attr_adv_pct 13.9 高于目标 10.0
  - [observe] 章内自我复读 17 句（如「她知道这把钥匙不是普通的钥匙，它是打开某个秘密的…」）
- 第 3 章：
  - 单条套路句式超限：「林婉儿的」×4、「为什么会」×4、「“我不知道」×3
  - narration_para_pct 6.3 低于目标 20.0
  - [observe] attr_adv_pct 20.8 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×4
  - narration_para_pct 6.8 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - dialogue_run_mean 13.1 高于目标 10.0
- 第 5 章：
  - narration_para_pct 19.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14710
chapter_chars_mean: 2942
chapter_chars_median: 3458
chapter_chars_cv: 0.35
paragraphs_mean: 78
dialogue_chars_pct: 39.8
dialogue_para_pct: 79.4
interiority_para_pct: 8.6
narration_para_pct: 11.9
turn_under20_pct: 82.6
turn_over200_pct: 0.0
attr_say_pct: 26.6
attr_adv_pct: 12.3
scenes_per_chapter: 7
dialogue_run_mean: 6.1
turn_len_median: 10
```
