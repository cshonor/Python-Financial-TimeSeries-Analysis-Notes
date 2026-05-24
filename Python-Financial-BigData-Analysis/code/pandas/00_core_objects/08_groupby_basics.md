# 08 GroupBy 基础（分组统计 / 分组变换 / 分组排名）
  
`groupby` 是量化最核心的工具之一：  
  
- 做 **分组统计**（行业内均值、日内分层收益）
- 做 **多股票独立计算**（每只股票自己的收益率、滚动指标）
- 做 **截面排名**（每个交易日对因子排序）
  
## 1. 分组统计（聚合）
  
- `df.groupby('industry')['ret'].mean()`
- 多指标聚合：`agg({'ret':'mean','vol':'sum'})`
  
## 2. 分组变换（transform）
  
`transform` 会返回与原 DataFrame **同长度** 的结果，适合生成新列。
  
- 行业中性化常用：`x - x.mean()`
  
## 3. 分组排名（rank）
  
- 截面分组：按 `date` 分组，对因子 `rank(pct=True)`
  
## 4. 常见坑
  
- `apply` 很强但可能慢；能用 `agg/transform` 就别用 `apply`
- 分组后 index 结构会变化，必要时 `reset_index()`
  
