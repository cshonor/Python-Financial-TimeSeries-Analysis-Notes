# Merge / Concat / Join（进阶版：多键、校验、重复键、时间对齐）

> 本文件是 **进阶版**：基础概念见 `00_core_objects/07_dataframe_merge_concat_join.md`。这里专注量化里最容易踩坑的“多表对齐 + 键的唯一性 + 合并后的数据质量”。

## 1. 多键合并：`on=['date','code']`

多资产数据（长表）最常见的主键是：

- `date`（交易日）
- `code`（股票代码）

合并价格表与因子表时，通常是：

```python
pd.merge(price, factor, on=['date','code'], how='left')
```

关键点：

- 主键应当尽量“能唯一定位一行”
- 合并前先检查键是否重复：`df.duplicated(['date','code']).sum()`

## 2. `how` 选择：你到底要保留谁？

- `left`：以左表为基准（最常用：价格为基准，补因子/行业）
- `inner`：只保留两边都有的数据（容易把停牌/缺失日直接删掉）
- `outer`：全保留（方便排查缺失来源，但 NaN 会多）

## 3. 合并校验（强烈建议）：`validate=...`

这是“防止数据悄悄错掉”的利器：

- `validate='one_to_one'`
- `validate='one_to_many'`
- `validate='many_to_one'`

示例（因子表每个 `(date,code)` 应该只有一条）：

```python
pd.merge(price, factor, on=['date','code'], how='left', validate='one_to_one')
```

如果键重复，它会直接报错，避免你带着错误数据继续回测。

## 4. 合并后必做的数据质量检查

合并完成后建议固定做三步：

- **行数是否异常膨胀**：重复键会导致笛卡尔积
- **缺失值规模**：`isna().sum()`（哪些字段对不齐？）
- **键是否仍唯一**：`duplicated(['date','code']).sum()`

## 5. 时间序列对齐（量化专用提醒）

“日期一样”不等于“交易日历一样”：

- 指数、个股、期货可能交易日不一致
- 财报/公告是低频数据，需要向前填充到交易日

常见做法：

- 低频字段合并后按 `code` 分组 `ffill`
- 或用“发布日期”与“生效日期”明确对齐，避免未来函数

## 6. `concat(axis=1)` 的高级用法：索引对齐 + 列名管理

横向拼接适合“同一 index 下补列”：

```python
pd.concat([df_price, df_factor], axis=1)
```

前提：

- index 必须是同一套（例如都以 `date` 为索引）
- 否则会出现大量 NaN（不是错，但你要知道为什么）

