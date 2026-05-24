# Python-Time-Series-Forecast

对应教材：**《Python 时间序列预测》**。

本册侧重：**交易日历、重采样、滚动/扩展窗口、信号 shift 对齐、时序规整**（对接 ARIMA / Prophet / statsmodels 等预测流程的前置数据处理）。

## 目录说明

| 子目录 | 用途 |
|--------|------|
| `docs/` | 原书章节笔记（[`docs/README.md`](./docs/README.md)） |
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

## 章节笔记（`docs/`）

| 章节 | 笔记 | 脚本 |
|------|------|------|
| 第 1 章 了解时间序列预测 | [docs/chapter01_time_series_forecasting_intro.md](./docs/chapter01_time_series_forecasting_intro.md) | [code/chapter01_forecast_workflow_demo.py](./code/chapter01_forecast_workflow_demo.py) |
| 第 2 章 基线预测 | [docs/chapter02_baseline_forecasting.md](./docs/chapter02_baseline_forecasting.md) | [code/chapter02_baseline_forecast_demo.py](./code/chapter02_baseline_forecast_demo.py) |
| 第 3 章 随机游走 | [docs/chapter03_random_walk.md](./docs/chapter03_random_walk.md) | [code/chapter03_random_walk_demo.py](./code/chapter03_random_walk_demo.py) |

## 建议学习顺序

1. 第 1 章：`docs/chapter01_*` + `code/chapter01_forecast_workflow_demo.py`  
2. 第 2 章：`docs/chapter02_*` + `code/chapter02_baseline_forecast_demo.py`  
3. 第 3 章：`docs/chapter03_*` + `code/chapter03_random_walk_demo.py`  
4. [`code/time_series_quant/`](./code/time_series_quant/) 专题（与 pandas 第 11 章并行）  
5. 后续按原书章节在 `docs/` 中追加  

**前置**：`../Python-Data-Analysis/docs/chapter11_time_series.md`、`../Python-Data-Analysis/code/numpy/`、`../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/`。
