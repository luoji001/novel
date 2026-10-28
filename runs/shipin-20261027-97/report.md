# 铁锹 生成报告

slug：`shipin-20261027-97`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7366
LLM 调用：57 次，累计 145.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 暖宝宝的温度 | 919 | short | 96.3 | 0 |  | 0 |
| 2 | 暖宝宝的重量 | 1490 | normal | 95.5 | 0 |  | 2 |
| 3 | 雪地里的金属碰撞 | 1100 | normal | 92.4 | 0 |  | 0 |
| 4 | 暖宝宝的温度 | 1361 | normal | 36.7 | 0 |  | 2 |
| 5 | 铁锹与雪铲的较量 | 1222 | normal | 36.8 | 0 |  | 1 |
| 6 | 钥匙的裂痕 | 1268 | normal | 91.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 24.0 低于目标 35.0
  - [observe] 标题与《暖宝宝的温度》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 6 句（如「周磊怒吼，“这车值多少钱你知道吗…」）
  - [observe] 标题重复：「暖宝宝的温度」已存在
- 第 5 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 6 章：
  - 情节与已写章节重复 0.65 ≥ 0.62（撞上「陈浩为夺回备用钥匙与周磊在停车场激烈对峙，最终用雪掩护找…」）

## 整书结构指标

```
chapters: 6
total_chars: 6761
chapter_chars_mean: 1127
chapter_chars_median: 1156
chapter_chars_cv: 0.18
paragraphs_mean: 42.7
dialogue_chars_pct: 29.3
dialogue_para_pct: 59.6
interiority_para_pct: 0.0
narration_para_pct: 40.4
turn_under20_pct: 97.5
turn_over200_pct: 0.0
attr_say_pct: 42.2
attr_adv_pct: 5.7
scenes_per_chapter: 1.5
dialogue_run_mean: 2.5
turn_len_median: 8
```
