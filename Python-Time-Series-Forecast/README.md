# Python-Time-Series-Forecast

对应教材：**《Python 时间序列预测》**。

本册侧重：时间序列预测工作流、经典 ARIMA/SARIMA、深度学习时序模型、Prophet，以及 **交易日历 / 重采样 / 滚动窗口 / shift 防前瞻** 等量化前置处理。

## 目录架构（按章拆分）

全书 **21 章**，每章独立文件夹，内含：

| 子目录 / 文件 | 说明 |
|---------------|------|
| `chapterNN_*.md` | **章总览**（章节总览、速查、演示、量化衔接、自检） |
| `code/` | 本章配套可运行脚本 |

书级共享资源（跨章专题）：

| 路径 | 说明 |
|------|------|
| [`code/time_series_quant/`](./code/time_series_quant/) | 时序量化专题（resample、rolling、shift 等） |

## 章节索引

| 章 | 总览 | 配套代码 |
|----|------|----------|
| 第 1 章 了解时间序列预测 | [chapter01/chapter01_time_series_forecasting_intro.md](./chapter01/chapter01_time_series_forecasting_intro.md) | [chapter01/code/](./chapter01/code/) |
| 第 2 章 基线预测 | [chapter02/chapter02_baseline_forecasting.md](./chapter02/chapter02_baseline_forecasting.md) | [chapter02/code/](./chapter02/code/) |
| 第 3 章 随机游走 | [chapter03/chapter03_random_walk.md](./chapter03/chapter03_random_walk.md) | [chapter03/code/](./chapter03/code/) |
| 第 4 章 移动平均 MA | [chapter04/chapter04_moving_average_process.md](./chapter04/chapter04_moving_average_process.md) | [chapter04/code/](./chapter04/code/) |
| 第 5 章 自回归 AR | [chapter05/chapter05_autoregressive_process.md](./chapter05/chapter05_autoregressive_process.md) | [chapter05/code/](./chapter05/code/) |
| 第 6 章 ARMA 建模 | [chapter06/chapter06_arma_modeling.md](./chapter06/chapter06_arma_modeling.md) | [chapter06/code/](./chapter06/code/) |
| 第 7 章 ARIMA | [chapter07/chapter07_arima_nonstationary.md](./chapter07/chapter07_arima_nonstationary.md) | [chapter07/code/](./chapter07/code/) |
| 第 8 章 SARIMA 季节性 | [chapter08/chapter08_sarima_seasonality.md](./chapter08/chapter08_sarima_seasonality.md) | [chapter08/code/](./chapter08/code/) |
| 第 9 章 SARIMAX 外生变量 | [chapter09/chapter09_sarimax_exogenous.md](./chapter09/chapter09_sarimax_exogenous.md) | [chapter09/code/](./chapter09/code/) |
| 第 10 章 VAR 多变量 | [chapter10/chapter10_var_multivariate.md](./chapter10/chapter10_var_multivariate.md) | [chapter10/code/](./chapter10/code/) |
| 第 11 章 顶点项目 | [chapter11/chapter11_capstone_aus_drugs.md](./chapter11/chapter11_capstone_aus_drugs.md) | [chapter11/code/](./chapter11/code/) |
| 第 12 章 深度学习入门 | [chapter12/chapter12_deep_learning_intro.md](./chapter12/chapter12_deep_learning_intro.md) | [chapter12/code/](./chapter12/code/) |
| 第 13 章 数据窗口与基线 | [chapter13/chapter13_data_window_baselines.md](./chapter13/chapter13_data_window_baselines.md) | [chapter13/code/](./chapter13/code/) |
| 第 14 章 线性模型与 DNN | [chapter14/chapter14_linear_and_dnn.md](./chapter14/chapter14_linear_and_dnn.md) | [chapter14/code/](./chapter14/code/) |
| 第 15 章 LSTM | [chapter15/chapter15_lstm.md](./chapter15/chapter15_lstm.md) | [chapter15/code/](./chapter15/code/) |
| 第 16 章 CNN | [chapter16/chapter16_cnn.md](./chapter16/chapter16_cnn.md) | [chapter16/code/](./chapter16/code/) |
| 第 17 章 ARLSTM | [chapter17/chapter17_arlstm.md](./chapter17/chapter17_arlstm.md) | [chapter17/code/](./chapter17/code/) |
| 第 18 章 DL 顶点项目 | [chapter18/chapter18_capstone_household_power.md](./chapter18/chapter18_capstone_household_power.md) | [chapter18/code/](./chapter18/code/) |
| 第 19 章 Prophet | [chapter19/chapter19_prophet.md](./chapter19/chapter19_prophet.md) | [chapter19/code/](./chapter19/code/) |
| 第 20 章 收官顶点 | [chapter20/chapter20_capstone_steak_price.md](./chapter20/chapter20_capstone_steak_price.md) | [chapter20/code/](./chapter20/code/) |
| 第 21 章 全书总结 | [chapter21/chapter21_beyond_self_summary.md](./chapter21/chapter21_beyond_self_summary.md) | [chapter21/code/](./chapter21/code/) |

## `code/time_series_quant/` 专题索引

| 文件 | 主题 |
|------|------|
| `01_datetime_index_and_trading_calendar.md` | 时间索引与交易日 |
| `02_resample_and_frequency_conversion.md` | 重采样与频率转换 |
| `03_rolling_window_operations.md` | 滚动窗口 |
| `04_expanding_window_operations.md` | 扩展窗口 |
| `05_shift_and_signal_alignment.md` | shift 与防未来函数 |
| `06_signal_generation_from_price.md` | 从价格生成信号 |

## 建议学习顺序

1. `chapter01/` → `chapter08/`（经典时序建模主线）  
2. `chapter09/` → `chapter11/`（外生变量、VAR、综合案例）  
3. `chapter12/` → `chapter21/`（深度学习 + Prophet + 收官）  
4. 并行精读 [`code/time_series_quant/`](./code/time_series_quant/)（与 pandas 第 11 章能力对齐）

**前置**：[`../Python-Data-Analysis/chapter11/`](../Python-Data-Analysis/chapter11/)、[`../Python-Data-Analysis/code/numpy/`](../Python-Data-Analysis/code/numpy/)、[`../Python-Financial-BigData-Analysis/code/pandas/`](../Python-Financial-BigData-Analysis/code/pandas/)。

## 运行示例

```bash
python Python-Time-Series-Forecast/chapter01/code/chapter01_forecast_workflow_demo.py
python Python-Time-Series-Forecast/chapter07/code/chapter07_arima_demo.py
```
