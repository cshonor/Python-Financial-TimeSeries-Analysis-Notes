# 时间重采样与频率转换
将时间序列在不同周期之间转换，用于多周期策略与降噪。

## 日线转周线
`python
df_weekly = df.resample('W').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})
`

## 分钟线转日线
`python
df_daily = df_minute.resample('D').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})
`

## 日线转月线
`python
df_monthly = df.resample('M').last()
`

## 在量化中的用途
- 多周期策略
- 周线/月线级别的回测
- 降低高频数据噪声
- 基本面数据与价格数据对齐
