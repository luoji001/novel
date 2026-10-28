# 铜钥匙 生成报告

slug：`shipin-20261027-284`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7007
LLM 调用：57 次，累计 143.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 船票上的铅笔字 | 851 | short | 38.4 | 0 |  | 3 |
| 2 | 钥匙上的名字 | 1359 | normal | 92.3 | 0 |  | 2 |
| 3 | 钥匙转动的瞬间 | 1046 | normal | 36.4 | 0 |  | 1 |
| 4 | 钥匙划破晨雾 | 1267 | normal | 90.6 | 0 |  | 0 |
| 5 | 手链滑入衣袖 | 1190 | normal | 89.6 | 0 |  | 1 |
| 6 | 船票滑落的瞬间 | 1288 | normal | 91.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.0 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 28.0 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「你是不是有什么事瞒着我？…」）
- 第 5 章：
  - narration_para_pct 34.8 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6531
chapter_chars_mean: 1088
chapter_chars_median: 1148
chapter_chars_cv: 0.16
paragraphs_mean: 31.8
dialogue_chars_pct: 26.6
dialogue_para_pct: 62.9
interiority_para_pct: 0.7
narration_para_pct: 36.4
turn_under20_pct: 97.9
turn_over200_pct: 0.0
attr_say_pct: 53.2
attr_adv_pct: 7.5
scenes_per_chapter: 2.2
dialogue_run_mean: 3.1
turn_len_median: 10
```
