# 蓝布 生成报告

slug：`shipin-20261027-245`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5985
LLM 调用：57 次，累计 126.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手电筒照亮登记簿 | 744 | short | 94.9 | 0 |  | 0 |
| 2 | 皮箱坠地 | 669 | normal | 37.4 | 0 |  | 1 |
| 3 | 皮箱夹层信纸 | 1103 | normal | 91.0 | 0 |  | 0 |
| 4 | 手电筒照亮登记簿 | 1167 | normal | 88.5 | 0 |  | 3 |
| 5 | 皮箱撞车厢门 | 1256 | normal | 35.8 | 0 |  | 1 |
| 6 | 手电筒照亮登记簿 | 1040 | normal | 90.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到李海在火车站找回父亲遗留的黑色皮箱，第三章又说在候车厅找回，地点不一致。  
2. 第三章提到用一块蓝布换取箱子归还，但小林的道具是蓝色登记簿，未提及蓝布。  
3. 第五章提到李海为带走箱子与老周争执，但第四章和第六章均提到李海为找回箱子与老周对峙，逻辑重复且时间线混乱。  
4. 第六章提到在阳光下打开箱子，但前文未交代箱子是否被锁或是否已归还。  
5. 第二章提到发现遗书，但第三章提到箱子被要求处理，未交代遗书是否被保留或处理。

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 622 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 19.2 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 标题重复：「手电筒照亮登记簿」已存在
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「我父亲临终前说过，只有找到这个箱子，才能解开他的…」）
- 第 6 章：
  - [observe] 标题重复：「手电筒照亮登记簿」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5580
chapter_chars_mean: 930
chapter_chars_median: 988
chapter_chars_cv: 0.25
paragraphs_mean: 25.8
dialogue_chars_pct: 25.1
dialogue_para_pct: 52.4
interiority_para_pct: 0.7
narration_para_pct: 46.9
turn_under20_pct: 95.3
turn_over200_pct: 0.0
attr_say_pct: 55.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.5
turn_len_median: 10
```
