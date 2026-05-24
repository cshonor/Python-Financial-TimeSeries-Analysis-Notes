# GroupBy 与聚合（进阶版：多维分组 / agg 命名 / transform / 分层回测）

> 本文件是 **进阶版**：默认你已经掌握 `00_core_objects/08_groupby_basics.md` 的基础语法。这里专注量化常用的“复杂分组 + 稳定输出 + 可回测结构”。

## 1. 多列分组：`groupby(['date','industry'])`

量化里最常见的两类分组：

- **时间截面分组**：`groupby('date')`（每天做一次截面统计/排名/分层）
- **多维分组**：`groupby(['date','industry'])`（每天在行业内做标准化/排名）

关键点：

- 你得到的是“分组对象”，最终输出结构会受 `as_index`、`sort` 影响
- 分组键是否唯一，会决定后面 unstack/pivot 的可用性

## 2. `agg` 的正确打开方式：多指标、命名输出、可读结果

### 2.1 单列多函数

```python
df.groupby('date')['ret'].agg(['mean', 'std', 'count'])
```

### 2.2 多列多函数（字典写法）

```python
df.groupby('date').agg({'ret': ['mean', 'std'], 'volume': 'sum'})
```

### 2.3 推荐：命名聚合（最清晰、最稳定）

```python
df.groupby('date').agg(
    ret_mean=('ret', 'mean'),
    ret_std=('ret', 'std'),
    vol_sum=('volume', 'sum'),
)
```

命名聚合的优势：

- 输出列名可控，不会生成多级列索引（少踩坑）
- 更适合落盘、画图、回测对接

## 3. `transform`：返回与原表等长（生成新列必备）

与 `agg` 不同，`transform` 的结果长度与原 DataFrame 相同，常用于“分组后回填到每一行”：

- **行业中性（简化版）**：`x - group_mean`
- **组内标准化**：\((x-\mu)/\sigma\)
- **组内 rank**：常用 `rank(pct=True)`

示例（行业内去均值）：

```python
df['factor_neutral'] = df['factor'] - df.groupby(['date','industry'])['factor'].transform('mean')
```

## 4. 截面分层回测：`qcut` 分组 + `unstack` 变成收益曲线矩阵

典型流程（每天按因子把股票分 5 组）：

1. `groupby('date')['factor'].rank(pct=True)` 计算截面分位
2. `qcut` 或分位阈值得到 `group`
3. `groupby(['date','group'])['ret_next'].mean()` 得到每组收益
4. `unstack()` 变成 “行=日期，列=分组” 的收益矩阵

注意：

- **收益必须是未来一期**（比如次日收益 `ret_next`），否则就是未来函数
- 分层前先处理缺失值和极端值，否则分位会失真

## 5. 性能与坑（你会真的遇到）

- **优先用 `agg/transform`，少用 `apply`**：`apply` 灵活但慢
- 分组键里有 `NaN`：默认会被丢到一个“缺失组”之外（行为依版本/参数），建议提前处理
- `groupby(..., sort=False)`：大数据时能省一点时间，但输出顺序要自己保证

