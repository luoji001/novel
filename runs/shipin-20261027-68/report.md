# 硬币与钥匙 生成报告

slug：`shipin-20261027-68`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7149
LLM 调用：57 次，累计 134.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币与纸条的对峙 | 777 | short | 38.5 | 0 |  | 1 |
| 2 | 硬币与空格的对峙 | 1508 | normal | 93.6 | 0 |  | 1 |
| 3 | 硬币与玻璃的对峙 | 1269 | normal | 37.2 | 0 |  | 2 |
| 4 | 钥匙与硬币的对峙 | 1166 | normal | 92.5 | 0 |  | 2 |
| 5 | 登记表上的指纹 | 1116 | normal | 91.1 | 0 |  | 0 |
| 6 | 硬币与登记表的对峙 | 1307 | normal | 94.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「今天早上去练车，记得带这个…」）
- 第 2 章：
  - [observe] 标题与《硬币与纸条的对峙》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「你怎么知道我在等你？…」）
  - [observe] 标题与《硬币与空格的对峙》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - [observe] 标题与《硬币与空格的对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 25.7 低于目标 35.0
  - [observe] 标题与《硬币与空格的对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6717
chapter_chars_mean: 1120
chapter_chars_median: 1142
chapter_chars_cv: 0.21
paragraphs_mean: 27.5
dialogue_chars_pct: 17.8
dialogue_para_pct: 54.8
interiority_para_pct: 1.3
narration_para_pct: 43.9
turn_under20_pct: 95.2
turn_over200_pct: 0.0
attr_say_pct: 22.3
attr_adv_pct: 2.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.5
turn_len_median: 8
```
