# 灯灭 生成报告

slug：`xiaoyuan-20261020-52`
档位：校园青春　闸门模式：observe
章数：9　总字数：21094
LLM 调用：100 次，累计 440.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表上的名字 | 1682 | short | 96.0 | 0 |  | 3 |
| 2 | 校服衣领的褶皱 | 2459 | normal | 29.2 | 0 |  | 2 |
| 3 | 磁带滑落的瞬间 | 2712 | normal | 92.0 | 0 |  | 2 |
| 4 | 指尖划过空位 | 2137 | normal | 94.0 | 0 |  | 1 |
| 5 | 纸条飘出书包缝隙 | 2460 | normal | 83.4 | 0 |  | 2 |
| 6 | 指纹印在通报纸上 | 2573 | normal | 92.8 | 0 |  | 2 |
| 7 | 纸条飘出书包缝隙 | 2502 | normal | 85.3 | 0 |  | 3 |
| 8 | 书包带勾住校服外套 | 3063 | normal | 85.1 | 0 |  | 2 |
| 9 | 指纹印在通报纸上 | 1497 | short | 86.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 14.7 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「陈老师转过身来，目光温和地看着她：“当然可以…」）
- 第 2 章：
  - dialogue_chars_pct 11.5 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「此刻，他更在意的是放在自己书包里的那张缴费单，那…」）
- 第 3 章：
  - 单条套路句式超限：「他知道自己」×4、「周野点了点头」×3、「”周野低」×3
  - narration_para_pct 11.3 低于目标 15.0
- 第 4 章：
  - narration_para_pct 12.5 低于目标 15.0
- 第 5 章：
  - dialogue_chars_pct 15.8 低于目标 20.0
  - [observe] 章内自我复读 10 句（如「而在另一边，周野则拿起桌上的笔，在纸上写下一行小…」）
- 第 6 章：
  - narration_para_pct 9.8 低于目标 15.0
  - [observe] 章内自我复读 2 句（如「你还记得我们第一次见面的情景吗？…」）
- 第 7 章：
  - 单条套路句式超限：「知道自己」×3
  - dialogue_chars_pct 17.1 低于目标 20.0
  - [observe] 标题重复：「纸条飘出书包缝隙」已存在
- 第 8 章：
  - [observe] 章内自我复读 35 句（如「周野把课本放回桌子里，眼睛依然停留在那本书包的边…」）
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「林夏点点」×3
  - narration_para_pct 12.9 低于目标 15.0
  - [observe] 章内自我复读 12 句（如「周野怔住了，他一直以为林夏是个很坚强的女孩，没想…」）
  - [observe] 标题重复：「指纹印在通报纸上」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19952
chapter_chars_mean: 2217
chapter_chars_median: 2364
chapter_chars_cv: 0.2
paragraphs_mean: 48.9
dialogue_chars_pct: 25.3
dialogue_para_pct: 62.1
interiority_para_pct: 16.7
narration_para_pct: 21.1
turn_under20_pct: 87.8
turn_over200_pct: 0.0
attr_say_pct: 53.1
attr_adv_pct: 6.9
scenes_per_chapter: 2.7
dialogue_run_mean: 2.9
turn_len_median: 10
```
