# 04 DataFrame 基础（结构 / 创建 / 列操作 / 行列索引）
  
DataFrame 是二维表格结构：**多列 Series 共享同一行索引**。它是量化研究中最常用的数据容器（K线、财务、因子、回测结果）。
  
## 1. 创建 DataFrame（常见方式）
  
- **字典 of 列**：`pd.DataFrame({'open': [...], 'close': [...]}, index=...)`
- **列表 of 行**：`pd.DataFrame([[...],[...]], columns=...)`
- **从 CSV/Excel 读取**：读取后再处理 index 和 dtype
  
## 2. 基本结构要点
  
- `df.index`：行索引（常见是日期 `DatetimeIndex`）
- `df.columns`：列索引（字段名）
- `df.values`：底层 ndarray（不建议随便用，容易丢失列名和对齐语义）
  
## 3. 列操作（最常用）
  
- `df['close']`：取列（返回 Series）
- `df[['open','close']]`：取多列（返回 DataFrame）
- `df['ret'] = df['close'].pct_change()`：新增列（收益率）
  
## 4. 行列选择（先记住两件事）
  
- **按标签**：`loc`（日期、代码等标签）
- **按位置**：`iloc`（第几行/第几列）
  
