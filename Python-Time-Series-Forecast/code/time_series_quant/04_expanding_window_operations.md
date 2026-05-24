# 扩展窗口操作
扩展窗口从序列起点开始，一直扩展到当前时点，使用全部历史数据进行计算。
常用于累计收益、最大回撤等分析。

## 常用写法
`python
# 累计收益率
df['cumulative_return'] = df['daily_return'].add(1).cumprod()

# 至今为止的最高价
df['highest_so_far'] = df['high'].expanding().max()

# 至今为止的最低价
df['lowest_so_far'] = df['low'].expanding().min()

# 扩展均值
df['expanding_mean'] = df['close'].expanding().mean()
`

## 在量化中的用途
- 最大回撤计算
- 历史高低点突破策略
- 累计收益分析
- 长期趋势判断
