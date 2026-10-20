# 红光误扫 生成报告

slug：`xuanyi-20261019-217`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15808
LLM 调用：68 次，累计 236.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描枪的红点 | 1625 | short | 98.0 | 0 |  | 1 |
| 2 | 扫描枪的红点 | 4526 | normal | 92.3 | 0 |  | 4 |
| 3 | 扫描枪的异常光斑 | 3903 | normal | 90.2 | 0 |  | 1 |
| 4 | 签名栏的空白 | 4012 | normal | 91.6 | 0 |  | 3 |
| 5 | 扫描枪的异常光斑 | 1737 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×4、「知道自己」×3
  - attr_adv_pct 17.2 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「双重扫描情况尚未明确说明…」）
  - [observe] 标题重复：「扫描枪的红点」已存在
- 第 3 章：
  - 单条套路句式超限：「林振东点点」×5、「林振东的」×4、「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×3、「陈雪梅点」×3
  - narration_para_pct 16.0 低于目标 20.0
  - [observe] attr_adv_pct 23.3 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 17.1 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
  - [observe] 标题重复：「扫描枪的异常光斑」已存在

## 整书结构指标

```
chapters: 5
total_chars: 15013
chapter_chars_mean: 3003
chapter_chars_median: 3729
chapter_chars_cv: 0.44
paragraphs_mean: 71.6
dialogue_chars_pct: 32.7
dialogue_para_pct: 68.5
interiority_para_pct: 9.5
narration_para_pct: 22.0
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 35.5
attr_adv_pct: 16.5
scenes_per_chapter: 4
dialogue_run_mean: 3.4
turn_len_median: 11
```
