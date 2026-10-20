# 磁带 生成报告

slug：`xiaoyuan-20261020-20`
档位：校园青春　闸门模式：observe
章数：9　总字数：20855
LLM 调用：100 次，累计 444.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 病历卡的触碰 | 1245 | short | 38.8 | 0 |  | 2 |
| 2 | 手指抚过公告栏 | 2550 | normal | 90.8 | 0 |  | 2 |
| 3 | 手指抚过磁带封皮 | 3025 | normal | 11.7 | 0 |  | 3 |
| 4 | 校服外套的重量 | 2379 | normal | 83.5 | 0 |  | 2 |
| 5 | 手指拂过课表边缘 | 2417 | normal | 91.1 | 0 |  | 4 |
| 6 | 手指拂过公告栏 | 2477 | normal | 85.8 | 0 |  | 4 |
| 7 | 手指抚过分科表 | 2658 | normal | 91.9 | 0 |  | 1 |
| 8 | 磁带消失的瞬间 | 2604 | normal | 87.3 | 0 |  | 3 |
| 9 | 手指拂过公告栏 | 1491 | short | 90.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.1 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「窗外的蝉鸣越来越急，林夏看着程野的背影，想起自己…」）
- 第 2 章：
  - 单条套路句式超限：「林夏站在」×3
  - dialogue_chars_pct 18.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「点了点头」×4
  - dialogue_chars_pct 9.4 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「有时候他会给我讲一些关于人生哲理的故事，有时也会…」）
- 第 4 章：
  - dialogue_chars_pct 17.9 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「她一直在努力让自己看起来很开心，可是在这一刻，她…」）
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×3
  - narration_para_pct 12.3 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「那你为什么总是躲着我？…」）
- 第 6 章：
  - 单条套路句式超限：「带着一丝」×3
  - dialogue_chars_pct 17.6 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「他只是继续翻着课本，好像完全没有听懂她的问题…」）
  - [observe] 标题与《手指抚过公告栏》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「林夏站在」×3
- 第 8 章：
  - 单条套路句式超限：「知道自己」×3、「为什么会」×3
  - dialogue_chars_pct 19.7 低于目标 20.0
  - [observe] 章内自我复读 8 句（如「她不知道自己为什么会有这种感觉，好像丢掉的东西不…」）
- 第 9 章：
  - [observe] 标题重复：「手指拂过公告栏」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19837
chapter_chars_mean: 2204
chapter_chars_median: 2364
chapter_chars_cv: 0.25
paragraphs_mean: 48.3
dialogue_chars_pct: 18.8
dialogue_para_pct: 60.4
interiority_para_pct: 19.7
narration_para_pct: 19.9
turn_under20_pct: 94.6
turn_over200_pct: 0.0
attr_say_pct: 42.9
attr_adv_pct: 4.1
scenes_per_chapter: 2.2
dialogue_run_mean: 2.6
turn_len_median: 8
```
