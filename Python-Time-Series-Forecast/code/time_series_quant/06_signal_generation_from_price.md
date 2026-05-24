# 从价格数据生成交易信号
从原始K线数据到可交易信号的完整流程。

## 步骤1：计算价格变动
`python
df['price_diff'] = df['close'] - df['close'].shift(1)
`

## 步骤2：标记上涨/下跌
`python
df['is_up'] = (df['price_diff'] > 0).astype(int)
`

## 步骤3：信号对齐，避免未来函数
`python
df['signal'] = df['is_up'].shift(1)
`

## 步骤4：计算策略收益
`python
df['strategy_return'] = df['signal'] * df['daily_return']
`

## 步骤5：计算累计收益
`python
df['strategy_cum_return'] = df['strategy_return'].add(1).cumprod()
`

## 总结
这是几乎所有趋势、反转策略的基础信号流程。
