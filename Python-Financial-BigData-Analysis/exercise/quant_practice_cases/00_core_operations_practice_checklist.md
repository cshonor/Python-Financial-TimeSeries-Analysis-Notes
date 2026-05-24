# 00 Pandas 四类核心操作（量化练习清单：选 / 改 / 算 / 拼）

> 目标：把 Pandas 当成“表格批处理工具”来用，而不是背 API。  
> 你只要反复练这四类动作，就能覆盖量化数据处理的 80%。

---

## 0. 练习数据（你会在配套 `00_core_operations_practice_checklist.py` 里直接生成）

- **价格 K 线表（df_price）**：`date, open, high, low, close, volume`
- **因子表（df_factor）**：`date, factor`
- **（可选）多资产长表（df_multi）**：`date, code, close, factor`

---

## 1) 选（筛选 / 取列 / 切片 / 条件）

量化里你每天都在“选”：

- **取列**
  - `df['close']`、`df[['open','close']]`
- **按日期切片（时间序列）**
  - `df.loc['2025-01-01':'2025-03-01']`
- **条件过滤（信号/异常）**
  - `df[df['volume'] > 0]`
  - `df[df['ret'].abs() < 0.1]`（粗略剔除极端值）

练习题：

- 选出“收盘价大于开盘价”的日期
- 选出“成交量在分位数 80% 以上”的日期
- 选出“最近 20 天”的子表

---

## 2) 改（清洗 / 新增列 / 类型 / 缺失值）

量化常见“改”：

- **新增列**
  - `df['ret'] = df['close'].pct_change()`
- **类型转换**
  - `pd.to_datetime(df['date'])`
  - `pd.to_numeric(..., errors='coerce')`
- **缺失值处理**
  - 时间序列常用：`ffill()`

练习题：

- 把 `date` 变成索引，并保证按时间升序
- 构造一个缺失的 `factor`，用 `ffill` 填充
- 用 `clip` 把收益率截断到 \([-0.2, 0.2]\)（演示“风控式清洗”）

---

## 3) 算（聚合 / 窗口 / 分组）

量化里“算”就是指标与统计：

- **滚动窗口**
  - `rolling(20).mean()`（均线）
  - `rolling(20).std()`（波动率）
- **shift 对齐（避免未来函数）**
  - 信号用 `shift(1)` 对齐到“下一根 K 线执行”
- **分组（多资产）**
  - `groupby('code').pct_change()`（每只股票独立收益）
  - `groupby('date')['factor'].rank(pct=True)`（截面分位）

练习题：

- 计算 20 日均线与 20 日波动率
- 生成“均线上穿”的交易信号，并 `shift(1)` 对齐
- 在多资产长表上：按 `date` 做截面 rank，选前 20%

---

## 4) 拼（合并 / 拼接 / 对齐）

量化里最容易“悄悄错掉”的地方就是拼表：

- **按键 merge（最常见）**
  - `pd.merge(df_price, df_factor, on='date', how='left', validate='one_to_one')`
- **按索引 join / concat(axis=1)**
  - 要求 index 对齐，否则会出现大量 NaN（不一定是错，但必须知道原因）

练习题：

- 把因子表合并进价格表，并用 `validate` 防止重复键
- 合并后检查缺失值规模：`isna().sum()`
- 把“多资产长表”透视成“收益宽表”（进阶：再 stack 回来）

---

## 最终检验（写量化的人必须有的 3 个自检）

- **是否未来函数**：信号是否严格只用过去数据（关键：`shift(1)`）
- **是否对齐正确**：merge/concat 后行数有没有异常膨胀、缺失值是否可解释
- **是否结构清晰**：长表做回测（groupby），宽表做矩阵（相关/协方差）

