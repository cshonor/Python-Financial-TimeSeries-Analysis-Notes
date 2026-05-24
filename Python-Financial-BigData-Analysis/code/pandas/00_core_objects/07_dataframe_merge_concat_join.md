# 07 合并与拼接（concat / merge / join）
  
量化研究经常需要把不同来源的数据拼在一起：
  
- 行方向拼接：把多个时间段的数据接起来
- 列方向合并：把价格、因子、行业、财务字段合成一张表
  
## 1. `concat`：按轴拼接（更像“堆叠”）
  
- 纵向拼：`pd.concat([df1, df2], axis=0)`
- 横向拼：`pd.concat([df1, df2], axis=1)`（按 index 对齐）
  
常用参数：
  
- `axis=0/1`
- `ignore_index=True`（不保留原 index）
  
## 2. `merge`：按键连接（更像 SQL join）
  
- `pd.merge(left, right, on='date', how='inner')`
- `how`: `inner/left/right/outer`
  
## 3. `join`：按 index 连接（merge 的简化）
  
- `df1.join(df2, how='left')`
  
## 4. 量化常见坑
  
- 时间序列合并一定要确认：**index/键是否同频率、是否同交易日历**
- 合并后检查 `isna().sum()`，缺失值可能来自“对不齐”
  
