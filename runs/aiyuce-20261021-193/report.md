# 笔锋 生成报告

slug：`aiyuce-20261021-193`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11859
LLM 调用：57 次，累计 221.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | AI写作设备屏幕 | 2006 | normal | 95.5 | 0 |  | 1 |
| 2 | 报价单上的数字 | 2183 | normal | 91.1 | 0 |  | 1 |
| 3 | 抄袭检测报告 | 2327 | normal | 36.8 | 0 |  | 3 |
| 4 | 签字笔的签名痕迹 | 1925 | normal | 90.3 | 0 |  | 2 |
| 5 | 营业执照的摩挲 | 2143 | normal | 36.4 | 0 |  | 1 |
| 6 | AI写作设备屏幕 | 1269 | short | 91.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - narration_para_pct 29.4 低于目标 45.0
- 第 3 章：
  - 单条套路句式超限：「临泉县教育局」×3
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 22.1 高于目标 18.0
  - narration_para_pct 26.3 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 7.7 低于目标 45.0
  - [observe] 标题重复：「AI写作设备屏幕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11561
chapter_chars_mean: 1927
chapter_chars_median: 2029
chapter_chars_cv: 0.19
paragraphs_mean: 16.7
dialogue_chars_pct: 13.4
dialogue_para_pct: 53.9
interiority_para_pct: 13.8
narration_para_pct: 32.4
turn_under20_pct: 64.9
turn_over200_pct: 0.0
attr_say_pct: 16.5
attr_adv_pct: 4.3
scenes_per_chapter: 2.3
dialogue_run_mean: 2.2
turn_len_median: 16
```
