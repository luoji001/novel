# 磁带 生成报告

slug：`xiaoyuan-20261020-43`
档位：校园青春　闸门模式：observe
章数：9　总字数：20654
LLM 调用：100 次，累计 429.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带塞进课桌夹层 | 1673 | short | 91.8 | 0 |  | 2 |
| 2 | 钥匙藏入储物柜缝隙 | 2440 | normal | 89.8 | 0 |  | 2 |
| 3 | 磁带滑落控制面板 | 2410 | normal | 95.1 | 0 |  | 2 |
| 4 | 分科表的张贴 | 2558 | normal | 91.8 | 0 |  | 1 |
| 5 | 落叶飘进书包缝隙 | 2897 | normal | 90.7 | 0 |  | 1 |
| 6 | 袖口裂痕提醒过往 | 2409 | normal | 85.6 | 0 |  | 2 |
| 7 | 撕碎的日记在掌心 | 2293 | normal | 90.1 | 0 |  | 2 |
| 8 | 钥匙藏入储物柜缝隙 | 2255 | normal | 91.9 | 0 |  | 2 |
| 9 | 撕碎的日记在掌心 | 1710 | short | 52.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 9.4 低于目标 15.0
  - [observe] 章内自我复读 18 句（如「你还记得那天下午吗？你在操场上走来走去，我正好也…」）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
  - [observe] 章内自我复读 17 句（如「他皱眉看了眼四周，教室里人声嘈杂，大家都在埋头做…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 9.3 低于目标 15.0
- 第 4 章：
  - interiority_para_pct 7.1 低于目标 8.0
- 第 5 章：
  - dialogue_chars_pct 19.0 低于目标 20.0
- 第 6 章：
  - dialogue_chars_pct 17.7 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「这时，广播声忽然响起：“请同学们注意，下周开始进…」）
- 第 7 章：
  - 单条套路句式超限：「林夏点点」×4、「林夏站在」×3
  - [observe] 章内自我复读 4 句（如「她知道，这一切都将随风而去，但她也会把它们珍藏在…」）
- 第 8 章：
  - narration_para_pct 14.0 低于目标 15.0
  - [observe] 标题重复：「钥匙藏入储物柜缝隙」已存在
- 第 9 章：
  - [observe] 章内自我复读 29 句（如「林夏望着窗外，那里有一群学生正在操场上奔跑，他们…」）
  - [observe] 标题重复：「撕碎的日记在掌心」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19545
chapter_chars_mean: 2172
chapter_chars_median: 2283
chapter_chars_cv: 0.17
paragraphs_mean: 51.6
dialogue_chars_pct: 24.5
dialogue_para_pct: 64.2
interiority_para_pct: 14.8
narration_para_pct: 20.9
turn_under20_pct: 90.5
turn_over200_pct: 0.0
attr_say_pct: 44.1
attr_adv_pct: 0.8
scenes_per_chapter: 2.4
dialogue_run_mean: 3.2
turn_len_median: 9
```
