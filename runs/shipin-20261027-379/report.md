# 蛇皮袋 生成报告

slug：`shipin-20261027-379`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6991
LLM 调用：57 次，累计 139.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋在两人间晃荡 | 709 | short | 95.2 | 0 |  | 0 |
| 2 | 水壶砸碎玻璃窗 | 1418 | normal | 37.4 | 0 |  | 2 |
| 3 | 钥匙串撞碎玻璃窗 | 1162 | normal | 37.0 | 0 |  | 1 |
| 4 | 笔记本压在香烟下 | 1110 | normal | 90.3 | 0 |  | 1 |
| 5 | 香烟坠入尘埃中 | 1355 | normal | 94.3 | 0 |  | 0 |
| 6 | 铁皮饭盒敲响地面 | 1231 | normal | 90.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - interiority_para_pct 6.4 高于目标 6.0
  - [observe] 章内自我复读 1 句（如「李建国没有回应，只是低头看着自己沾满泥污的手，像…」）
- 第 3 章：
  - [observe] 章内自我复读 4 句（如「他向前走了一步，背影有些佝偻，却依然保持着一种固…」）
- 第 4 章：
  - interiority_para_pct 8.3 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 6529
chapter_chars_mean: 1088
chapter_chars_median: 1132
chapter_chars_cv: 0.22
paragraphs_mean: 30
dialogue_chars_pct: 18.5
dialogue_para_pct: 51.8
interiority_para_pct: 3.1
narration_para_pct: 45.1
turn_under20_pct: 99.3
turn_over200_pct: 0.0
attr_say_pct: 23.2
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.7
turn_len_median: 8
```
