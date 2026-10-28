# 红灯下的录像带 生成报告

slug：`shipin-20261027-65`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6264
LLM 调用：57 次，累计 122.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙转动的瞬间 | 510 | short | 37.0 | 0 |  | 3 |
| 2 | 钥匙落地的瞬间 | 1135 | normal | 36.8 | 0 |  | 2 |
| 3 | 钥匙转动的瞬间 | 1484 | normal | 90.0 | 0 |  | 1 |
| 4 | 皮夹机关的轻响 | 975 | normal | 91.3 | 0 |  | 0 |
| 5 | 扫帚划破夜色 | 985 | normal | 90.9 | 0 |  | 0 |
| 6 | 钥匙坠入深潭 | 1169 | normal | 90.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.7 低于目标 5.0
  - narration_para_pct 94.1 高于目标 90.0
  - [observe] 章节过短 461 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「一个声音响起，低沉但平稳…」）
  - [observe] 标题与《钥匙转动的瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 标题重复：「钥匙转动的瞬间」已存在
- 第 6 章：
  - narration_para_pct 33.3 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5820
chapter_chars_mean: 970
chapter_chars_median: 984
chapter_chars_cv: 0.32
paragraphs_mean: 29.2
dialogue_chars_pct: 17.6
dialogue_para_pct: 39.5
interiority_para_pct: 1.8
narration_para_pct: 58.8
turn_under20_pct: 96.1
turn_over200_pct: 0.0
attr_say_pct: 36.7
attr_adv_pct: 0.0
scenes_per_chapter: 2.7
dialogue_run_mean: 1.6
turn_len_median: 8
```
