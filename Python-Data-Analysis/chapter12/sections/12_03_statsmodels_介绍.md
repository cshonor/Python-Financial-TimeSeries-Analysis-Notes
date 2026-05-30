# 12.3 statsmodels 介绍

> 所属：[第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md) · 《利用 Python 进行数据分析》

---

### 12.3 statsmodels 介绍

- 导入：`import statsmodels.api as sm`，`import statsmodels.formula.api as smf`。
- 线性/GLM/混合效应、ANOVA、时间序列等。

#### 基础 OLS 线性回归

- **数组 API**：`sm.add_constant(X)` → `sm.OLS(y, X).fit()`。
- **公式 API（推荐）**：`smf.ols('y ~ col0 + col1', data=df).fit()`，自动截距与列名。
- **`results.summary()`**：R²、F 检验、系数、p 值、置信区间等。
- **`results.predict(new_data)`** 预测。

---

[← 返回第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md)
