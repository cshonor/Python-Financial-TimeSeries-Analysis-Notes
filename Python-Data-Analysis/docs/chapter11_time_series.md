# 第 11 章 时间序列

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 11 章。  
> 时间序列是在多个时间点重复观测的结构化数据，广泛用于金融、经济等领域。本章讲解 pandas 的 **DatetimeIndex / Period、切片与移位、时区、重采样、移动窗口** 等工具。

**前置**：[第 10 章 数据聚合与分组](./chapter10_data_aggregation_groupby.md) → 本章 → [第 12 章 建模库](./chapter12_modeling_libraries_patsy_statsmodels.md)。

**本仓库深化练习**（时序量化专题）：

| 主题 | 路径 |
|------|------|
| 交易日历 / DatetimeIndex | [`../../Python-Time-Series-Forecast/code/time_series_quant/01_datetime_index_and_trading_calendar.md`](../../Python-Time-Series-Forecast/code/time_series_quant/01_datetime_index_and_trading_calendar.md) |
| 重采样 | [`../../Python-Time-Series-Forecast/code/time_series_quant/02_resample_and_frequency_conversion.md`](../../Python-Time-Series-Forecast/code/time_series_quant/02_resample_and_frequency_conversion.md) |
| 滚动窗口 | [`../../Python-Time-Series-Forecast/code/time_series_quant/03_rolling_window_operations.md`](../../Python-Time-Series-Forecast/code/time_series_quant/03_rolling_window_operations.md) |
| 扩展窗口 / shift | [`04_expanding_window_operations.md`](../../Python-Time-Series-Forecast/code/time_series_quant/04_expanding_window_operations.md)、[`05_shift_and_signal_alignment.md`](../../Python-Time-Series-Forecast/code/time_series_quant/05_shift_and_signal_alignment.md) |

**演示脚本**：[`../code/chapter11_time_series_demo.py`](../code/chapter11_time_series_demo.py)

---

## 章节总览

**小节统计**（资料自 11.2 起）：7 个一级模块 + 15 个二级小节，共 **22 个详细小节**（含 11.1 引言性内容）。

| 一级 | 二级 |
|------|------|
| 11.1～11.2 时间序列基础 | 11.2.1 索引选取；11.2.2 重复索引 |
| 11.3 日期范围与移位 | 11.3.1～11.3.3 |
| 11.4 时区 | — |
| 11.5 时期 Period | 11.5.1～11.5.4 |
| 11.6 重采样 | 11.6.1～11.6.4 |
| 11.7 移动窗口 | 11.7.1～11.7.3 |
| 11.8 总结 | — |

---

## 一、书本原文核心知识点提炼

### 11.1 / 11.2 时间序列基础

- 形式：时间戳、固定周期、时间区间、试验时长等。
- **`DatetimeIndex`** + **`Timestamp`**（`datetime64[ns]` 纳秒精度）。

#### 11.2.1 索引、选取、子集构造

- 索引可用 `datetime` 或日期字符串（`"2011-01-10"`）。
- **`"2001"`** / **`"2001-05"`** 切片整年/整月。
- 时间切片多为**视图**（修改影响原数据）；也可用 **`truncate(before=, after=)`**。

#### 11.2.2 重复索引

- **`index.is_unique`** 判断是否重复；重复标签索引返回**切片**而非标量。
- 聚合：`groupby(level=0).mean()` 等同时间点合并。

### 11.3 日期范围、频率与移位

#### 11.3.1 生成日期范围

- **`pd.date_range(start, end, periods=, freq="D")`**；`freq="BM"` 等工作日规则。
- **`normalize=True`**：对齐到午夜。

#### 11.3.2 频率与偏移量

- 别名：`"H"`, `"M"`, `"BM"`… 对应 `Hour`, `MonthEnd` 等 **Offset** 类。
- 倍数：`"4H"`、`"1h30min"`；锚定偏移如月末。
- **`rollforward` / `rollback`**：将日期滚到频率边界。

#### 11.3.3 shift

- **`shift(n)`**：索引不动，**数值**移位 → 首尾 NA；用于 `ts / ts.shift(1) - 1`。
- **`shift(n, freq="D")`**：数值不动，**索引**移位。

### 11.4 时区

- 夏令时（DST）复杂；pandas 集成 **pytz**，如 `"America/New_York"`、`tz_localize` / `tz_convert`、UTC。

### 11.5 时期 Period

- **Period** = 时间段（如 2012 全年）；与 Timestamp（点）相对。

#### 11.5.1 频率转换

- **`period.asfreq("M", how="start"|"end")`** 子/父周期转换。

#### 11.5.2 季度周期

- 财季：`Q-JAN` … `Q-DEC`（如 `Q-JAN` 下 2012Q4 含义依财年末定义）。

#### 11.5.3 时间戳 ↔ 周期

- **`to_period()`**、**`to_timestamp()`**；周期不重叠，可能产生重复周期标签。

#### 11.5.4 PeriodIndex 构造

- **`pd.PeriodIndex(year=..., quarter=..., freq="Q-DEC")`** 从分列拼装。

### 11.6 重采样 resample

#### 11.6.1 降采样

- 高频 → 低频，类似 groupby；**`closed`**（左/右闭合）、**`label`**（区间用起点还是终点作标签）。
- 金融：**`resample("...").ohlc()`** 开高低收。

#### 11.6.2 升采样与插值

- 低频 → 高频产生间隙；**`.asfreq()`** 后 **`ffill()` / `bfill()`**，`limit` 限制填充长度。

#### 11.6.3 Period 重采样

- 降采样目标频率须为**子周期**；升采样须为**父周期**，否则报错。

#### 11.6.4 分组时间重采样

- **`groupby([pd.Grouper(freq="5min"), "code"]).mean()`** 分类键 + 时间频率联合聚合。

### 11.7 移动窗口

- **`rolling(window)`**：按窗口长度或 `"20D"` 滑动；**`expanding()`** 从起点累积扩大。
- 默认跳过 NA；**`min_periods`** 控制最少有效观测数。

#### 11.7.1 指数加权

- **`ewm(span=...)`**：近期权重更大（EMA）。

#### 11.7.2 二元移动窗口

- **`s1.rolling(...).corr(s2)`** 滚动相关等。

#### 11.7.3 自定义

- **`rolling(...).apply(func)`**：窗口内约简为标量（如分位数）。

### 11.8 总结

- 下一章：[第 12 章 Patsy 与 statsmodels](./chapter12_modeling_libraries_patsy_statsmodels.md)。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 日期索引 | `pd.to_datetime`, `pd.DatetimeIndex` |
| 切片 | `ts["2020"]`, `ts["2020-03":"2020-05"]` |
| 日期范围 | `pd.date_range("2025-01-01", periods=10, freq="B")` |
| 收益 | `close.pct_change()` 或 `close / close.shift(1) - 1` |
| 降采样 | `ts.resample("W").mean()`, `.ohlc()` |
| 升采样填值 | `ts.resample("D").ffill()` |
| 滚动均值 | `ts.rolling(20).mean()` |
| EMA | `ts.ewm(span=12).mean()` |
| 联合重采样 | `df.groupby([pd.Grouper(freq="M"), "code"]).sum()` |

---

## 三、通用基础示例

见 [`../code/chapter11_time_series_demo.py`](../code/chapter11_time_series_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **交易日历**：A 股用 `freq="B"` 或自定义 `CustomBusinessDay`；勿把周末当缺失随意 `ffill`。
2. **日频 OHLC**：分钟线 `resample("1D").ohlc()` 生成日线；注意 `closed`/`label` 与交易所切片一致。
3. **复权价 shift**：用复权收盘价算收益；`shift(1)` 对齐“昨日收盘 → 今日收益”。
4. **滚动波动率**：`ret.rolling(20).std() * np.sqrt(252)` 年化；`min_periods` 避免上市初期虚假值。
5. **EMA / MACD**：`ewm` 建快慢线；参数与交易软件一致时需核对 `adjust`。
6. **多标的**：长表 `groupby("code")` 内 `rolling` 或 `Grouper`；宽表对每列分别 rolling。
7. **宏观月度对齐**：`PeriodIndex` / `to_period("M")` 再 merge 到日频行情（注意发布滞后）。
8. **时区**：全球市场统一 UTC 存储，展示再 `tz_convert`。

---

## 五、与 statsmodels 建模的衔接要点

- **平稳性**：建模前常对价格取对数差分或收益率；`diff()` / `pct_change` 与 `shift` 等价关系要分清。
- **频率一致**：`resample` 到月频再跑 `ARIMA`；日频与月频混用会错配样本量。
- **滚动回归**：`rolling.apply` 可做时变 beta；正式推断更常用 statsmodels 的滚动/状态空间接口。
- **避免未来函数**：信号用 `shift(1)`；因子对齐见时序专题 [`05_shift_and_signal_alignment.md`](../../Python-Time-Series-Forecast/code/time_series_quant/05_shift_and_signal_alignment.md)。
- 第 12 章起：将清洗后的 **DatetimeIndex Series** 传入 `statsmodels.tsa` 等模块。

---

## 本章自检清单

- [ ] 会用日期字符串切片与 `truncate`  
- [ ] 会用 `date_range`、`shift` 算收益  
- [ ] 会用 `resample` 降采样 / OHLC  
- [ ] 会用 `rolling` / `ewm`  
- [ ] 了解 `Grouper` + `groupby`  
- [ ] 知道 Period 与时区的基本用途  

---

## 后续扩展留白

### 11.2～11.7

（留白）
