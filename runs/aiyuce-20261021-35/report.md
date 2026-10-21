# 文件夹 生成报告

slug：`aiyuce-20261021-35`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10663
LLM 调用：55 次，累计 207.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面的指尖 | 1797 | normal | 37.1 | 0 |  | 3 |
| 2 | 陈立指着报价单 | 2013 | normal | 33.4 | 0 |  | 3 |
| 3 | 敲击桌面的指尖 | 1681 | normal | 82.8 | 0 |  | 4 |
| 4 | 屏幕上的误判率数据 | 2354 | normal | 35.0 | 0 |  | 1 |
| 5 | 陈立指着表格 | 1916 | normal | 32.0 | 0 |  | 5 |
| 6 | 敲击桌面的指尖 | 896 | short | 84.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 34.5 高于目标 18.0
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 42.9 高于目标 18.0
  - narration_para_pct 32.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 65.2 高于目标 18.0
  - dialogue_run_mean 6.3 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0
  - [observe] 标题重复：「敲击桌面的指尖」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 66.4 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「此时，在办公室另一端传来一阵键盘敲击声，几个助理…」）
  - [observe] 标题与《陈立指着报价单》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 38.8 高于目标 18.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 标题重复：「敲击桌面的指尖」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10316
chapter_chars_mean: 1719
chapter_chars_median: 1798
chapter_chars_cv: 0.28
paragraphs_mean: 20.8
dialogue_chars_pct: 42.7
dialogue_para_pct: 65.3
interiority_para_pct: 3.1
narration_para_pct: 31.6
turn_under20_pct: 33.8
turn_over200_pct: 0.0
attr_say_pct: 17.0
attr_adv_pct: 3.6
scenes_per_chapter: 1.7
dialogue_run_mean: 4.1
turn_len_median: 30
```
