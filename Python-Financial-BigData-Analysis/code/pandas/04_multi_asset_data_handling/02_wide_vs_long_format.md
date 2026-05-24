# 宽表与长表格式转换
这两种格式是多标的数据最常见的存储方式，需熟练掌握互相转换。

## 格式对比
- **长表 (Long Format)**：每一行是一只股票在某一天的数据

`
date      | code      | close
2025-01-01| 000001.SZ | 10.5
2025-01-01| 000002.SZ | 20.3
`

- **宽表 (Wide Format)**：每一列是一只股票的时间序列

`
date      | 000001.SZ | 000002.SZ
2025-01-01| 10.5      | 20.3
`

## 互相转换
`python
# 长表 → 宽表
df_wide = df_long.pivot(index='date', columns='code', values='close')

# 宽表 → 长表
df_long = df_wide.stack().reset_index(name='close')
`

## 在量化中的用途
- 长表：方便做截面分组、因子回测
- 宽表：方便批量计算多只股票的收益率、指标
