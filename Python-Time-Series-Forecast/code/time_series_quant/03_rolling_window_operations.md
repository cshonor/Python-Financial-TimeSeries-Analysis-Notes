# 滚动窗口操作
滚动窗口计算是量化交易中技术指标的核心工具，它在时间序列上以固定长度滑动，计算各种统计量。

## 常用写法
`python
# 5日均线
df['ma5'] = df['close'].rolling(window=5).mean()

# 20日均线
df['ma20'] = df['close'].rolling(window=20).mean()

# 20日滚动标准差（波动率）
df['volatility_20'] = df['close'].rolling(20).std()

# 滚动最大值、最小值
df['highest_5'] = df['high'].rolling(5).max()
df['lowest_5'] = df['low'].rolling(5).min()

# 5日成交量之和
df['volume_5_sum'] = df['volume'].rolling(5).sum()
`

## 关键参数
- window：回看周期
- min_periods：最少需要多少个有效数据
- closed：控制窗口哪边闭合

## 在量化中的用途
- 均线策略
- RSI、MACD、布林带等指标计算
- 波动率衡量
- 趋势强度判断
