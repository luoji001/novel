# 雨靴的归属 生成报告

slug：`shipin-20261027-75`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6640
LLM 调用：57 次，累计 136.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴的归属 | 595 | short | 37.8 | 0 |  | 1 |
| 2 | 钥匙转动的瞬间 | 1204 | normal | 55.0 | 0 |  | 0 |
| 3 | 铁皮盒子的刻痕 | 1297 | normal | 36.6 | 0 |  | 1 |
| 4 | 雨靴裂开缝隙 | 1275 | normal | 86.4 | 0 |  | 4 |
| 5 | 钥匙划过门框 | 1219 | normal | 88.9 | 0 |  | 0 |
| 6 | 钥匙与老照片 | 1044 | normal | 87.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到“七号楼”，但第三章、第五章使用“七楼”而非“七号楼”，称呼不一致。  
2. 第六章提到“刘德昌在办公室发现一份旧房产证”，但前文未提及刘德昌有办公室。  
3. 第三章提到“刘德昌与李阿姨因一串旧物展开对过去居住权的争执”，但前文未明确交代刘德昌与李阿姨之间有直接关联。  
4. 第五章提到“周建国用一把生锈的钥匙打开了尘封多年的老房子”，但第二章已提到“周建国用生锈的钥匙打开七号楼的旧门”，前后重复且未说明“老房子”与“七号楼”是否为同一地点。  
5. 第六章提到“将它归还给李阿姨”，但前文未明确交代“它”指代何物，导致指代不明。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 532 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 4 章：
  - dialogue_chars_pct 50.2 高于目标 45.0
  - narration_para_pct 14.0 低于目标 35.0
  - attr_adv_pct 12.5 高于目标 10.0
  - dialogue_run_mean 9.2 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6076
chapter_chars_mean: 1013
chapter_chars_median: 1131
chapter_chars_cv: 0.26
paragraphs_mean: 34.7
dialogue_chars_pct: 20.7
dialogue_para_pct: 44.8
interiority_para_pct: 1.6
narration_para_pct: 53.6
turn_under20_pct: 96.3
turn_over200_pct: 0.0
attr_say_pct: 49.0
attr_adv_pct: 8.1
scenes_per_chapter: 2
dialogue_run_mean: 2.8
turn_len_median: 10
```
