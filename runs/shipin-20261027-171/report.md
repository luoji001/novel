# 二维码 生成报告

slug：`shipin-20261027-171`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6207
LLM 调用：57 次，累计 141.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 数零钱 | 275 | short | 33.6 | 0 |  | 3 |
| 2 | 铁皮秤上的刻度线 | 912 | normal | 37.9 | 0 |  | 2 |
| 3 | 二维码贴纸断裂声 | 1374 | normal | 93.5 | 0 |  | 0 |
| 4 | 称粉 | 1355 | normal | 93.8 | 0 |  | 0 |
| 5 | 数零钱 | 1079 | normal | 93.4 | 0 |  | 1 |
| 6 | 铁皮秤上的数字停住 | 1206 | normal | 36.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第一章和第五章都名为《数零钱》，但内容和人物不同，存在标题重复但内容不一致的问题。  
2. 第六章提到“铁皮秤被调包”，但前文（第二章、第四章）只提到陈阿婆使用铁皮秤称粉，并未提及秤具被调包的情节，前后缺乏铺垫。  
3. 第五章提到“墙上写着欢迎光临的标语”，但前文未有相关描写，属于突然出现的细节，缺乏铺垫。  
4. 第三章提到“二维码贴纸断裂声”，但前文未提及陈阿婆使用二维码贴纸，属于突然引入的新元素，缺乏铺垫。  
5. 第六章提到“蓝帽男子”，但前文未有此人出现，属于突然引入的新角色，缺乏铺垫。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 246 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「老李，帮我看看有没有缺货…」）
  - [observe] 章节过短 804 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 标题重复：「数零钱」已存在
- 第 6 章：
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5741
chapter_chars_mean: 957
chapter_chars_median: 1062
chapter_chars_cv: 0.41
paragraphs_mean: 31.5
dialogue_chars_pct: 18.4
dialogue_para_pct: 49.1
interiority_para_pct: 0.5
narration_para_pct: 50.4
turn_under20_pct: 92.9
turn_over200_pct: 0.0
attr_say_pct: 10.0
attr_adv_pct: 4.1
scenes_per_chapter: 2.5
dialogue_run_mean: 2.0
turn_len_median: 8
```
