# 数据移位与信号对齐
这是量化回测中**最重要的一节**，用于避免未来函数（未来信息）。

## 基础移位用法
`python
# 前一日收盘价
df['prev_close'] = df['close'].shift(1)

# 下一日开盘价
df['next_open'] = df['open'].shift(-1)
`

## 正确的信号生成方式
`python
# 计算日收益率
df['daily_return'] = df['close'].pct_change()

# 错误写法：用今天收益生成今天信号 → 未来函数
df['signal'] = np.where(df['daily_return'] > 0, 1, 0)

# 正确写法：用昨天收益生成今天信号 → 无未来数据
df['signal'] = np.where(df['daily_return'].shift(1) > 0, 1, 0)
`

## 核心逻辑
- 今日信号只能用**过去的数据**计算
- 交易在下一根K线执行
- shift(1) 是避免未来函数的标准做法

这是回测是否真实有效的根本规则。
