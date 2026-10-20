# 旧钟的指针 生成报告

slug：`xuanyi-20261019-89`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13734
LLM 调用：68 次，累计 227.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿的指纹 | 1363 | short | 97.0 | 0 |  | 1 |
| 2 | 挂钟的停滞时光 | 3947 | normal | 90.1 | 0 |  | 5 |
| 3 | 摩挲钢笔的木纹 | 3189 | normal | 88.8 | 0 |  | 3 |
| 4 | 掀开海报的暗格 | 3640 | normal | 90.9 | 0 |  | 2 |
| 5 | 翻阅褪色登记簿 | 1590 | short | 90.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「婉秋，我需要你帮我查一下登记簿的内容…」）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×4、「苏婉秋点」×3、「带着一丝」×3
  - narration_para_pct 13.5 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
  - [observe] 章内自我复读 14 句（如「她皱起眉头，仔细核对了一遍签字簿里的内容，又对着…」）
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×6、「林振邦的」×6、「“我不知道」×4
  - narration_para_pct 13.4 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「苏婉秋走进来，手里还拎着什么东西，“我前几天看到…」）
- 第 4 章：
  - 单条套路句式超限：「林振邦的」×5、「”苏婉秋低」×4、「这是什么？」×4
  - narration_para_pct 10.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林振邦的」×4
  - narration_para_pct 17.9 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13095
chapter_chars_mean: 2619
chapter_chars_median: 3040
chapter_chars_cv: 0.44
paragraphs_mean: 56
dialogue_chars_pct: 34.6
dialogue_para_pct: 73.1
interiority_para_pct: 10.9
narration_para_pct: 15.9
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 36.2
attr_adv_pct: 10.4
scenes_per_chapter: 2.8
dialogue_run_mean: 4.0
turn_len_median: 12
```
