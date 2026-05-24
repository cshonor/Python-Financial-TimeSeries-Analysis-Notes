# 06 DataFrame 排序与类型（sort_values / sort_index / astype）
  
排序与类型管理在量化研究里很“底层”，但非常关键：
  
- 时间序列必须按时间排序，否则 rolling/shift/resample 容易出错
- 数值列如果被读成 `object`，会导致计算慢、甚至结果错误
  
## 1. 按索引排序（时间序列常用）
  
- `df.sort_index()`：按行索引排序（日期）
- `df.sort_index(ascending=False)`：倒序
  
## 2. 按列排序（选股/排名常用）
  
- `df.sort_values('factor', ascending=False)`：按因子降序
- 多列排序：`sort_values(['date','factor'])`
  
## 3. 类型转换（读 CSV 后必做）
  
- `astype(float)` / `astype('int64')`
- `pd.to_datetime(df['date'])`：日期列转 datetime
  
## 4. 常见坑
  
- `NaN` 会影响排序（默认排到最后）
- `astype(int)` 遇到 NaN 会报错，先 `fillna` 或用 `Int64`（可空整数类型）
  
