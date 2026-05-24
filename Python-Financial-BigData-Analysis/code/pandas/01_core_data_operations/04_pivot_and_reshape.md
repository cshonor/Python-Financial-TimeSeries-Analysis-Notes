# Pivot & Reshape（进阶版：pivot_table 参数、缺失处理、超大宽表策略）

> 本文件是 **进阶版**：基础用法见 `00_core_objects/09_pivot_table_and_reshape.md`。这里补齐量化里真正会用到的复杂参数与坑。

## 1. `pivot` vs `pivot_table`：什么时候必须用 `pivot_table`

- `pivot`：要求 `(index, columns)` 组合唯一；重复就直接报错
- `pivot_table`：允许重复；会按 `aggfunc` 自动聚合（类似 Excel 数据透视表）

量化里你经常遇到重复：

- 分钟线聚合到日线（同一天多条）
- 同一天同一只股票重复记录（脏数据）

这时就用 `pivot_table` 并明确聚合逻辑（比如 `last`/`sum`/`mean`）。

## 2. `pivot_table` 关键参数（建议背下来）

```python
pd.pivot_table(
    df,
    values='close',
    index='date',
    columns='code',
    aggfunc='last',
    fill_value=None,
    margins=False,
    dropna=True,
)
```

- `aggfunc`：重复时怎么聚合（`last/sum/mean` 或自定义函数）
- `fill_value`：聚合后缺失填充（谨慎使用，别把缺失当真实值）
- `margins=True`：加总计（做报表时有用，回测通常不需要）
- `dropna`：是否丢掉全 NaN 的列/行（行为受版本影响，注意检查）

## 3. 多指标透视：values 多列 -> 多级列索引

当你同时透视 `close` 和 `volume`：

```python
pt = pd.pivot_table(
    df,
    values=['close', 'volume'],
    index='date',
    columns='code',
    aggfunc={'close': 'last', 'volume': 'sum'},
)
```

输出会变成多级列索引（MultiIndex columns）。常见处理：

- `pt.columns.names` 设置列层级名称
- 或在落盘前把列名拍平（例如用 `'close__000001'` 这种）

## 4. 超大宽表：什么时候别 pivot（内存会爆）

如果你有：

- 2000+ 股票
- 2000+ 交易日

pivot 成宽表相当于一个 2000x2000 的矩阵，再加多指标、多行业字段，内存会非常可观。

经验法则：

- **因子回测/分层回测**：优先用长表（`date,code,factor,ret`），用 `groupby` 解决
- **矩阵化运算（比如协方差、相关系数）**：才需要宽表

## 5. stack/unstack 的实战用途：在“矩阵”和“回测表”之间切换

- 宽表（收益矩阵） -> 长表（回测表）：`wide.stack().reset_index()`
- 长表（回测表） -> 宽表（收益矩阵）：`long.pivot(index='date', columns='code', values='ret')`

常见坑：

- `stack` 后的列名默认叫 `0`，记得 `reset_index(name='xxx')`
- `unstack` 会引入缺失（停牌/非交易日），回测前要明确怎么处理 NaN
