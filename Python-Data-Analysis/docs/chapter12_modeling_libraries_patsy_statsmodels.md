# 第 12 章 Python 建模库介绍

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 12 章。  
> 在加载、清洗、规整、可视化之后，本章完成从**数据处理**到**数据建模**的跨越，重点介绍 **Patsy**（公式 → 设计矩阵）与 **statsmodels**（频率论统计推断、时间序列）。  
> *注：你提供的资料片段未完整覆盖 12.1 与 scikit-learn 部分；本笔记以 Patsy + statsmodels 为核心，并预留 scikit-learn 扩展位。*

**前置**：[第 11 章 时间序列](./chapter11_time_series.md) → 本章 → [第 13 章 数据分析案例](./chapter13_data_analysis_case_studies.md)。

**本仓库专题**：[`../code/statsmodels/`](../code/statsmodels/)（待扩充示例）

**演示脚本**：[`../code/chapter12_statsmodels_demo.py`](../code/chapter12_statsmodels_demo.py)

---

## 章节总览

**小节统计**（基于当前资料）：2 个一级模块 + 3 个二级小节 + 独立操作块，共 **5 个核心知识块**。

| 一级 | 二级 / 模块 |
|------|-------------|
| 12.2 Patsy 模型描述 | 12.2.1 数据转换；12.2.2 分类数据 |
| 12.3 statsmodels | OLS 拟合；12.3.2 时间序列（AutoReg 等） |
| （资料未全）12.1 / scikit-learn | 留白 |

---

## 一、书本原文核心知识点提炼

### 12.2 用 Patsy 创建模型描述

- R/S 风格公式：`y ~ x0 + x1`（`+` 表示纳入设计矩阵项，非算术加）。
- **`patsy.dmatrices('公式', data)`** → `(y, X)`，`DesignMatrix` 为带元数据的 ndarray。
- 默认含 **`Intercept`** 截距列；去截距：`y ~ x0 + x1 + 0`。
- 矩阵可接 **`np.linalg.lstsq`** 等底层求解。

#### 12.2.1 用 Patsy 公式进行数据转换

- 公式内可写 Python 函数：`np.log(np.abs(x1) + 1)`。
- 内置 **`standardize`**、**`center`**（有状态：须用训练集统计量变换新数据）。
- 真算术相加用 **`I(x0 + x1)`** 封装。
- 预测新样本：**`patsy.build_design_matrices([X.design_info], new_data)`** 复用训练时的转换状态。

#### 12.2.2 分类数据和 Patsy

- 非数值列 → **虚拟变量**；有截距时去掉一个基准水平防共线。
- 无截距（`+ 0`）时保留全部哑变量列。
- **`C(列名)`** 强制按分类处理数值编码列。
- **`key1:key2`** 生成交互项（ANOVA 常用）。

### 12.3 statsmodels 介绍

- 导入：`import statsmodels.api as sm`，`import statsmodels.formula.api as smf`。
- 线性/GLM/混合效应、ANOVA、时间序列等。

#### 基础 OLS 线性回归

- **数组 API**：`sm.add_constant(X)` → `sm.OLS(y, X).fit()`。
- **公式 API（推荐）**：`smf.ols('y ~ col0 + col1', data=df).fit()`，自动截距与列名。
- **`results.summary()`**：R²、F 检验、系数、p 值、置信区间等。
- **`results.predict(new_data)`** 预测。

#### 12.3.2 对时间序列过程进行估计

- **`statsmodels.tsa`**：AR、状态空间、卡尔曼滤波等。
- **`AutoReg(endog, lags=MAXLAGS)`**：拟合自回归；可设较大最大滞后再由模型估计各阶系数。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 设计矩阵 | `patsy.dmatrices('y ~ x1 + C(ind)', data=df)` |
| 去截距 | `'y ~ x1 + 0'` |
| 标准化 | `'y ~ standardize(x1)'` |
| 新数据矩阵 | `build_design_matrices([design_info], new_df)` |
| OLS 公式 | `smf.ols('ret ~ pe + C(industry)', data).fit()` |
| OLS 数组 | `sm.OLS(y, sm.add_constant(X)).fit()` |
| 报告 | `fit.summary()` |
| AR | `AutoReg(series, lags=5).fit()` |

---

## 三、通用基础示例

见 [`../code/chapter12_statsmodels_demo.py`](../code/chapter12_statsmodels_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **截面因子回归**：`smf.ols('ret_fwd ~ factor + C(industry)', data=panel).fit()`，`ret_fwd` 用 `shift(-1)` 或下期收益（防未来函数见第 11 章）。
2. **Fama-French 风格**：多因子 + 行业固定效应；Patsy `C()` 与 `get_dummies(drop_first=True)` 二选一，勿重复编码。
3. **Newey-West 标准误**：`fit(cov_type='HAC', cov_kwds={'maxlags': 5})` 处理收益序列自相关（进阶，超出本章但实盘常用）。
4. **对数市值**：公式内 `np.log(market_cap)` 或 Patsy 自定义函数。
5. **AR 收益模型**：检验自相关后再定阶；与 ARIMA 模块衔接时序预测册。
6. **样本内外**：训练集 `fit`，`predict` 用 `build_design_matrices` 或 formula API 传入 OOS 数据。

---

## 五、与全书 pandas 工作流的衔接要点

| 阶段 | 章节 | 衔接 |
|------|------|------|
| 清洗 | 第 7 章 | `dropna`、异常值后再进模型 |
| 合并 | 第 8 章 | 因子与收益 `(date, code)` 对齐 |
| 分组 | 第 10 章 | 逐日 `groupby('date').apply(ols)` |
| 时序 | 第 11 章 | `AutoReg`、平稳性、`diff` |
| 可视化 | 第 9 章 | 残差图、`summary` 对照 |

- Patsy 与 pandas **`get_dummies`** 功能重叠：公式接口更贴近 R/Stata；手写矩阵更透明。
- **scikit-learn**（原书同章预告）：侧重预测与交叉验证；statsmodels 侧重**推断与诊断**，量化研究常两者并用。

---

## 本章自检清单

- [ ] 会用 `dmatrices` 理解 y / X 与截距  
- [ ] 知道 `standardize` 的有状态性与 `build_design_matrices`  
- [ ] 会用 `C()` 与交互项 `a:b`  
- [ ] 会用 `smf.ols(...).fit().summary()`  
- [ ] 了解 `AutoReg` 基本用法  

---

## 后续扩展留白

### 12.1 / scikit-learn

（留白：待补原书 scikit-learn 小节纪要）
