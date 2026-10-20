# 磁带 生成报告

slug：`xiaoyuan-20261020-91`
档位：校园青春　闸门模式：observe
章数：9　总字数：19756
LLM 调用：100 次，累计 431.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带消失在走廊拐角 | 1477 | short | 47.4 | 0 |  | 4 |
| 2 | 课表被揉皱 | 2665 | normal | 90.5 | 0 |  | 1 |
| 3 | 磁带消失在走廊拐角 | 2254 | normal | 92.4 | 0 |  | 2 |
| 4 | 指尖触碰校徽 | 2185 | normal | 83.4 | 0 |  | 1 |
| 5 | 矿泉水瓶的沉默时刻 | 2560 | normal | 0.0 | 0 |  | 2 |
| 6 | 指尖触碰校徽 | 2062 | normal | 94.1 | 0 |  | 1 |
| 7 | 指尖触碰校徽 | 2515 | normal | 86.9 | 0 |  | 3 |
| 8 | 分科表被风吹动 | 2631 | normal | 91.9 | 0 |  | 1 |
| 9 | 磁带掉落排水沟 | 1398 | short | 88.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林夏站在」×3、「林夏点点」×3
  - dialogue_chars_pct 15.1 低于目标 20.0
  - interiority_para_pct 7.7 低于目标 8.0
  - [observe] 章内自我复读 16 句（如「她向前走了几步，又回头望了一眼公告栏，那上面还贴…」）
- 第 2 章：
  - [observe] 章内自我复读 23 句（如「那张被揉皱的纸片他已经找不见了，只剩下脑海里的画…」）
- 第 3 章：
  - 单条套路句式超限：「到了一个」×3
  - [observe] 标题重复：「磁带消失在走廊拐角」已存在
- 第 4 章：
  - [observe] 章内自我复读 31 句（如「林夏看着他背影消失在楼梯拐角，忽然想起什么，转身…」）
- 第 5 章：
  - [observe] 章内自我复读 30 句（如「货架上整齐摆放着各类饮品，她盯着其中一瓶矿泉水看…」）
  - [observe] dialogue_chars_pct 7.5 < 8.0（结构塌缩）
- 第 6 章：
  - [observe] 标题重复：「指尖触碰校徽」已存在
- 第 7 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 19 句（如「桌面上那份教室容量统计表还在继续显示着各种数据，…」）
  - [observe] 标题重复：「指尖触碰校徽」已存在
- 第 8 章：
  - 单条套路句式超限：「教务处」×4
- 第 9 章：
  - dialogue_chars_pct 15.5 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 18810
chapter_chars_mean: 2090
chapter_chars_median: 2119
chapter_chars_cv: 0.22
paragraphs_mean: 43.6
dialogue_chars_pct: 20.5
dialogue_para_pct: 59.9
interiority_para_pct: 15.2
narration_para_pct: 24.9
turn_under20_pct: 92.9
turn_over200_pct: 0.0
attr_say_pct: 31.4
attr_adv_pct: 1.3
scenes_per_chapter: 2.7
dialogue_run_mean: 2.7
turn_len_median: 10
```
