# 纸飞机 生成报告

slug：`xiaoyuan-20261020-146`
档位：校园青春　闸门模式：observe
章数：9　总字数：20420
LLM 调用：100 次，累计 432.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 笔记本里的未寄出的字迹 | 1315 | short | 98.5 | 0 |  | 0 |
| 2 | 录音机嗡鸣重启 | 2537 | normal | 92.2 | 0 |  | 1 |
| 3 | 折痕后的未写完句子 | 2408 | normal | 85.9 | 0 |  | 3 |
| 4 | 纸飞机落满银杏叶 | 2602 | normal | 83.9 | 0 |  | 4 |
| 5 | 名单飘落 | 2382 | normal | 92.6 | 0 |  | 3 |
| 6 | 纸条藏进校服口袋 | 2474 | normal | 91.9 | 0 |  | 0 |
| 7 | 蓝色笔记本的第一页 | 2718 | normal | 90.3 | 0 |  | 1 |
| 8 | 手指拂过公告栏 | 2247 | normal | 90.0 | 0 |  | 3 |
| 9 | 未寄出的信纸 | 1728 | short | 84.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「林夏站在」×3
  - dialogue_chars_pct 16.5 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「她走路的时候总喜欢把书包带子甩来甩去，像一只不安…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林夏站在」×4
  - dialogue_chars_pct 17.0 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「就在这时，一位工作人员走了过来，打断了他们的谈话…」）
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×3
  - narration_para_pct 14.0 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - [observe] 章内自我复读 12 句（如「夕阳下的银杏叶在地上铺成一片金色的海洋，她踩上去…」）
- 第 8 章：
  - 单条套路句式超限：「林夏站在」×3、「林夏点点」×3
  - narration_para_pct 10.4 低于目标 15.0
  - [observe] 章内自我复读 8 句（如「陈老师说，“希望你能考进理想大学…」）
- 第 9 章：
  - dialogue_chars_pct 14.6 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 19413
chapter_chars_mean: 2157
chapter_chars_median: 2299
chapter_chars_cv: 0.2
paragraphs_mean: 47.7
dialogue_chars_pct: 22.0
dialogue_para_pct: 64.7
interiority_para_pct: 16.5
narration_para_pct: 18.8
turn_under20_pct: 90.2
turn_over200_pct: 0.0
attr_say_pct: 43.2
attr_adv_pct: 6.4
scenes_per_chapter: 2.8
dialogue_run_mean: 3.1
turn_len_median: 8
```
