# 模型灯 生成报告

slug：`aiyuce-20261021-132`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11261
LLM 调用：57 次，累计 219.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 表格与图纸的对话 | 1880 | normal | 35.6 | 0 |  | 4 |
| 2 | 标准差对比分析 | 2156 | normal | 34.7 | 0 |  | 4 |
| 3 | 示波器价格清单 | 1848 | normal | 34.8 | 0 |  | 3 |
| 4 | 软件采购与教学调整 | 2178 | normal | 35.6 | 0 |  | 1 |
| 5 | 计算器与问卷 | 2031 | normal | 34.0 | 0 |  | 3 |
| 6 | 表格边缘的铅笔痕迹 | 1162 | short | 34.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 28.1 高于目标 18.0
  - dialogue_run_mean 14 高于目标 4.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - 命中套话收尾句
  - dialogue_chars_pct 35.7 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这个问题直指张伟的教学方式调整…」）
- 第 3 章：
  - dialogue_chars_pct 34.7 高于目标 18.0
  - narration_para_pct 15.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「几天后，张伟向学校提出了增加设备的数量的请求，并…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 33.3 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 6 章：
  - dialogue_chars_pct 57.7 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 10955
chapter_chars_mean: 1826
chapter_chars_median: 1904
chapter_chars_cv: 0.2
paragraphs_mean: 17.2
dialogue_chars_pct: 30.7
dialogue_para_pct: 60.4
interiority_para_pct: 4.5
narration_para_pct: 35.1
turn_under20_pct: 29.4
turn_over200_pct: 0.0
attr_say_pct: 19.1
attr_adv_pct: 5.6
scenes_per_chapter: 1.5
dialogue_run_mean: 4.6
turn_len_median: 30
```
