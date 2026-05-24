# 分组回测实战
使用 groupby 是实现多股票策略、分层回测的基础。

## 等权组合收益
`python
# 每日所有股票的策略收益取平均，构建等权组合
portfolio_return = df.groupby('date')['strategy_return'].mean()
`

## 行业中性处理
`python
# 按日期和行业分组，计算行业内的因子暴露
df['industry_factor_rank'] = df.groupby(['date', 'industry'])['factor'].rank(pct=True)
`

## 分层回测（多因子策略）
`python
# 每日按因子值排序，分成5组
df['factor_quintile'] = df.groupby('date')['factor'].qcut(5, labels=False)

# 计算每一组的平均收益
group_return = df.groupby(['date', 'factor_quintile'])['return'].mean().unstack()
`
