# 09 透视表与变形（pivot / pivot_table / stack / unstack）
  
多资产数据经常在 **长表（long）** 和 **宽表（wide）** 之间转换：
  
- **长表**：`date, code, close` 每行一条记录（做分组、回测、分层方便）
- **宽表**：行是 date，列是 code（做矩阵化计算方便）
  
## 1. `pivot`：长表 -> 宽表（唯一键）
  
- `df.pivot(index='date', columns='code', values='close')`
  
要求：`(date, code)` 组合必须唯一，否则会报错。
  
## 2. `pivot_table`：允许重复（自动聚合）
  
- `df.pivot_table(index='date', columns='code', values='close', aggfunc='last')`
  
## 3. `stack/unstack`：宽长互转（MultiIndex）
  
- 宽 -> 长：`wide.stack().reset_index()`
- 长 -> 宽：`long.set_index(['date','code']).unstack('code')`
  
## 4. 常见坑
  
- 宽表列数多（几千只股票）时内存占用大；长表更通用
- 透视后要检查缺失（交易日不一致、停牌都会导致 NaN）
  
