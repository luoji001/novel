# 磁带 生成报告

slug：`xiaoyuan-20261020-86`
档位：校园青春　闸门模式：observe
章数：9　总字数：20042
LLM 调用：100 次，累计 426.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 名单上的红痕 | 1320 | short | 75.4 | 0 |  | 3 |
| 2 | 分科表的圈记 | 2678 | normal | 91.1 | 0 |  | 3 |
| 3 | 纸片上的未完故事 | 2289 | normal | 92.1 | 0 |  | 2 |
| 4 | 校服外套的破洞 | 2390 | normal | 92.3 | 0 |  | 0 |
| 5 | 磁带与疤痕的对望 | 2583 | normal | 53.3 | 0 |  | 3 |
| 6 | 课表的指尖触碰 | 2594 | normal | 88.0 | 0 |  | 3 |
| 7 | 麦克风的余温 | 2339 | normal | 87.6 | 0 |  | 1 |
| 8 | 信封边缘的指纹 | 2305 | normal | 87.5 | 0 |  | 4 |
| 9 | 倒计时牌的触感 | 1535 | short | 85.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 15.7 低于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 12 句（如「她看着陈老师将一张新的名单贴上去，纸张摩擦发出细…」）
- 第 2 章：
  - 单条套路句式超限：「知道自己」×4
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 章内自我复读 21 句（如「因为我看到你每天早到，也看到你总是最后一个离开教…」）
- 第 3 章：
  - 单条套路句式超限：「林夏站在」×4
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
- 第 5 章：
  - dialogue_chars_pct 14.4 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「她看着窗外飘落的树叶，忽然想起几个月前，她在操场…」）
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「不仅仅是」×4、「点了点头」×3、「他知道这」×3
  - [observe] 章内自我复读 16 句（如「就在她即将走出办公室的一刻，突然听见一个熟悉的声…」）
- 第 7 章：
  - [observe] 章内自我复读 20 句（如「周野的目光停留在她的眼睛里，仿佛看到了某种未曾说…」）
- 第 8 章：
  - 单条套路句式超限：「林夏点点」×4、「知道自己」×3、「林夏站在」×3
  - dialogue_chars_pct 19.6 低于目标 20.0
  - narration_para_pct 14.0 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「她不知道自己是否真的准备好面对这一切，但她隐约感…」）
- 第 9 章：
  - 单条套路句式超限：「林夏站在」×3、「国际部教务处」×3
  - dialogue_chars_pct 18.9 低于目标 20.0
  - narration_para_pct 7.7 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「林夏站在毕业典礼的倒计时牌前，看着上面的数字从“…」）

## 整书结构指标

```
chapters: 9
total_chars: 19079
chapter_chars_mean: 2120
chapter_chars_median: 2223
chapter_chars_cv: 0.21
paragraphs_mean: 45.6
dialogue_chars_pct: 23.0
dialogue_para_pct: 60.5
interiority_para_pct: 20.4
narration_para_pct: 19.1
turn_under20_pct: 86.1
turn_over200_pct: 0.0
attr_say_pct: 42.6
attr_adv_pct: 9.8
scenes_per_chapter: 2.8
dialogue_run_mean: 2.2
turn_len_median: 9
```
