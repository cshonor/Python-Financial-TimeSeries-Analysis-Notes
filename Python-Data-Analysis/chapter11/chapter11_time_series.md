# 第 11 章 时间序列

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 11 章。  
> 时间序列是在多个时间点重复观测的结构化数据，广泛用于金融、经济等领域。本章讲解 pandas 的 **DatetimeIndex / Period、切片与移位、时区、重采样、移动窗口** 等工具。

**前置**：[第 10 章 数据聚合与分组](../chapter10/chapter10_data_aggregation_groupby.md) → 本章 → [第 12 章 建模库](../chapter12/chapter12_modeling_libraries_patsy_statsmodels.md)。

**本仓库深化练习**（时序量化专题）：

| 主题 | 路径 |
|------|------|
| 交易日历 / DatetimeIndex | [`../../../Python-Time-Series-Forecast/code/time_series_quant/01_datetime_index_and_trading_calendar.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/01_datetime_index_and_trading_calendar.md) |
| 重采样 | [`../../../Python-Time-Series-Forecast/code/time_series_quant/02_resample_and_frequency_conversion.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/02_resample_and_frequency_conversion.md) |
| 滚动窗口 | [`../../../Python-Time-Series-Forecast/code/time_series_quant/03_rolling_window_operations.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/03_rolling_window_operations.md) |
| 扩展窗口 / shift | [`04_expanding_window_operations.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/04_expanding_window_operations.md)、[`05_shift_and_signal_alignment.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/05_shift_and_signal_alignment.md) |

**演示脚本**：[`./code/chapter11_time_series_demo.py`](./code/chapter11_time_series_demo.py)

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

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [11_01_11_2_时间序列基础](./sections/11_01_11_2_时间序列基础.md) | 11 2 时间序列基础 |
| [11_02_01_索引_选取_子集构造](./sections/11_02_01_索引_选取_子集构造.md) | 01 索引 选取 子集构造 |
| [11_02_02_重复索引](./sections/11_02_02_重复索引.md) | 02 重复索引 |
| [11_03_日期范围_频率与移位](./sections/11_03_日期范围_频率与移位.md) | 日期范围 频率与移位 |
| [11_03_01_生成日期范围](./sections/11_03_01_生成日期范围.md) | 01 生成日期范围 |
| [11_03_02_频率与偏移量](./sections/11_03_02_频率与偏移量.md) | 02 频率与偏移量 |
| [11_03_03_shift](./sections/11_03_03_shift.md) | 03 shift |
| [11_04_时区](./sections/11_04_时区.md) | 时区 |
| [11_05_时期_Period](./sections/11_05_时期_Period.md) | 时期 Period |
| [11_05_01_频率转换](./sections/11_05_01_频率转换.md) | 01 频率转换 |
| [11_05_02_季度周期](./sections/11_05_02_季度周期.md) | 02 季度周期 |
| [11_05_03_时间戳_周期](./sections/11_05_03_时间戳_周期.md) | 03 时间戳 周期 |
| [11_05_04_PeriodIndex_构造](./sections/11_05_04_PeriodIndex_构造.md) | 04 PeriodIndex 构造 |
| [11_06_重采样_resample](./sections/11_06_重采样_resample.md) | 重采样 resample |
| [11_06_01_降采样](./sections/11_06_01_降采样.md) | 01 降采样 |
| [11_06_02_升采样与插值](./sections/11_06_02_升采样与插值.md) | 02 升采样与插值 |
| [11_06_03_Period_重采样](./sections/11_06_03_Period_重采样.md) | 03 Period 重采样 |
| [11_06_04_分组时间重采样](./sections/11_06_04_分组时间重采样.md) | 04 分组时间重采样 |
| [11_07_移动窗口](./sections/11_07_移动窗口.md) | 移动窗口 |
| [11_07_01_指数加权](./sections/11_07_01_指数加权.md) | 01 指数加权 |
| [11_07_02_二元移动窗口](./sections/11_07_02_二元移动窗口.md) | 02 二元移动窗口 |
| [11_07_03_自定义](./sections/11_07_03_自定义.md) | 03 自定义 |
| [11_08_总结](./sections/11_08_总结.md) | 总结 |

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

见 [`./code/chapter11_time_series_demo.py`](./code/chapter11_time_series_demo.py)

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
- **避免未来函数**：信号用 `shift(1)`；因子对齐见时序专题 [`05_shift_and_signal_alignment.md`](../../../Python-Time-Series-Forecast/code/time_series_quant/05_shift_and_signal_alignment.md)。
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
