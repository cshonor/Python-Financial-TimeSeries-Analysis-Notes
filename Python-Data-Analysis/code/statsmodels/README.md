# Statsmodels 专题

> **《利用 Python 进行数据分析》第 12 章总笔记**：[`../../chapter12/chapter12_modeling_libraries_patsy_statsmodels.md`](../../chapter12/chapter12_modeling_libraries_patsy_statsmodels.md)  
> 章节演示脚本：[`../../chapter12/code/chapter12_statsmodels_demo.py`](../../chapter12/code/chapter12_statsmodels_demo.py)

Statsmodels 是 Python 的统计建模库，侧重计量经济学与统计学**推断**（系数、p 值、诊断检验）。

## 专题笔记

| 文件 | 说明 |
|------|------|
| [**statsmodels_vs_sklearn_quant.md**](./statsmodels_vs_sklearn_quant.md) | **statsmodels vs scikit-learn** 核心区别、股票量化分工、组合流程、案例与避坑 |

## 主要功能

- 回归分析（OLS、GLS、GLM、Logit/Probit 等）
- 时间序列（ARIMA、VAR、协整检验等）
- 假设检验、ANOVA、稳健标准误
- 描述性统计与模型诊断

## 与 scikit-learn 的分工（量化）

- **statsmodels**：因子显著性、归因、模型诊断 → 研究阶段  
- **scikit-learn**：特征工程、滚动预测、信号生成 → 交易阶段  
- 详见 [statsmodels_vs_sklearn_quant.md](./statsmodels_vs_sklearn_quant.md)

## 跨书衔接

- 计量推断深化：[`Using-Python-for-Introductory-Econometrics`](../../../Using-Python-for-Introductory-Econometrics/)
- 时序预测：[`Python-Time-Series-Forecast`](../../../Python-Time-Series-Forecast/)

## 学习资源

- [Statsmodels 官方文档](https://www.statsmodels.org/)
