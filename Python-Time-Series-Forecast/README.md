# Python-Time-Series-Forecast

对应教材：**《Python 时间序列预测》**。

本册侧重：**交易日历、重采样、滚动/扩展窗口、信号 shift 对齐、时序规整**（对接 ARIMA / Prophet / statsmodels 等预测流程的前置数据处理）。

## 目录说明

| 子目录 | 用途 |
|--------|------|
| `docs/` | 原书章节笔记（待按书本目录填充） |
| `code/time_series_quant/` | **当前主力**：从金融大数据册迁出的时序量化专题 |
| `dataset/` | 单标的 / 多频率样本序列 |
| `exercise/` | 预测与回测练习题 |
| `assets/` | 时序示意图、ACF/PACF 截图等 |

## `code/time_series_quant/` 文件索引

| 文件 | 主题 |
|------|------|
| `01_datetime_index_and_trading_calendar.md` | 时间索引与交易日 |
| `02_resample_and_frequency_conversion.md` | 重采样与频率转换 |
| `03_rolling_window_operations.md` | 滚动窗口 |
| `04_expanding_window_operations.md` | 扩展窗口 |
| `05_shift_and_signal_alignment.md` | shift 与防未来函数 |
| `06_signal_generation_from_price.md` | 从价格生成信号 |

前置建议：先完成 `../Python-Data-Analysis/docs/chapter11_time_series.md`（原书第 11 章）与 `../Python-Data-Analysis/code/numpy/`、`../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/`。
