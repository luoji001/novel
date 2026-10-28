# 铜推子 生成报告

slug：`shipin-20261027-58`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6510
LLM 调用：57 次，累计 136.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜质推子泛冷光 | 620 | short | 33.8 | 0 |  | 3 |
| 2 | 碎玻璃映晨光 | 1193 | normal | 93.5 | 0 |  | 0 |
| 3 | 布包上的洗发水泡沫 | 1344 | normal | 93.4 | 0 |  | 0 |
| 4 | 存折上的铜质推子 | 1274 | normal | 89.7 | 0 |  | 0 |
| 5 | 推子抵胸口 | 965 | normal | 92.1 | 0 |  | 2 |
| 6 | 铜质推子泛冷光 | 1108 | normal | 89.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 579 < 597（本章目标 1087 字的 55%）
- 第 5 章：
  - narration_para_pct 30.0 低于目标 35.0
  - dialogue_run_mean 4.7 高于目标 4.0
- 第 6 章：
  - [observe] 标题重复：「铜质推子泛冷光」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6151
chapter_chars_mean: 1025
chapter_chars_median: 1089
chapter_chars_cv: 0.25
paragraphs_mean: 22
dialogue_chars_pct: 19.7
dialogue_para_pct: 47.7
interiority_para_pct: 0.8
narration_para_pct: 51.5
turn_under20_pct: 87.6
turn_over200_pct: 0.0
attr_say_pct: 65.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.4
turn_len_median: 10
```
