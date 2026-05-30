# 12.2 用 Patsy 创建模型描述

> 所属：[第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md) · 《利用 Python 进行数据分析》

---

### 12.2 用 Patsy 创建模型描述

- R/S 风格公式：`y ~ x0 + x1`（`+` 表示纳入设计矩阵项，非算术加）。
- **`patsy.dmatrices('公式', data)`** → `(y, X)`，`DesignMatrix` 为带元数据的 ndarray。
- 默认含 **`Intercept`** 截距列；去截距：`y ~ x0 + x1 + 0`。
- 矩阵可接 **`np.linalg.lstsq`** 等底层求解。

---

[← 返回第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md)
