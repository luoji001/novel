# 校对尺 生成报告

slug：`aiyuce-20261021-188`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10999
LLM 调用：57 次，累计 213.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面的红笔 | 1891 | normal | 38.6 | 0 |  | 2 |
| 2 | 翻开工资表 | 1873 | normal | 35.8 | 0 |  | 1 |
| 3 | 翻看客户反馈报告 | 1985 | normal | 36.4 | 0 |  | 1 |
| 4 | 敲击键盘的手指 | 1784 | normal | 36.8 | 0 |  | 2 |
| 5 | 翻看财务报表 | 2014 | normal | 35.7 | 0 |  | 1 |
| 6 | 点击屏幕的指尖 | 1446 | short | 88.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「他停顿片刻，目光扫向旁边的一叠纸质账册，“如果按…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这条推论会被什么推翻？…」）
- 第 5 章：
  - [observe] 章内自我复读 6 句（如「听到这个问题后，陈晓阳只是摇了摇头，把那份最新的…」）
- 第 6 章：
  - narration_para_pct 40.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 10735
chapter_chars_mean: 1789
chapter_chars_median: 1842
chapter_chars_cv: 0.11
paragraphs_mean: 13.8
dialogue_chars_pct: 7.0
dialogue_para_pct: 31.6
interiority_para_pct: 14.2
narration_para_pct: 54.2
turn_under20_pct: 60.9
turn_over200_pct: 0.0
attr_say_pct: 7.9
attr_adv_pct: 7.9
scenes_per_chapter: 1.5
dialogue_run_mean: 2.0
turn_len_median: 14
```
