# MultiIndex 多级索引操作
MultiIndex 是处理多只股票数据的标准方式，通常以 (日期, 股票代码) 作为索引。

## 创建多级索引
`python
# 从列表创建
index = pd.MultiIndex.from_product([dates, codes], names=['date', 'code'])

# 从现有DataFrame设置
df_multi = df.set_index(['date', 'code'])
`

## 常用操作
`python
# 按日期切片（截面数据）
df_multi.xs('2025-01-01', level='date')

# 按股票代码切片（时间序列）
df_multi.xs('000001.XSHE', level='code')

# 按层级筛选
df_multi.loc[('2025-01-01', '000001.XSHE')]
`

## 在量化中的用途
- 多股票策略数据存储
- 截面因子分析
- 行业/市值分组回测
