# 第 12 章 Python 建模库介绍

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 12 章。  
> 在加载、清洗、规整、可视化之后，本章完成从**数据处理**到**数据建模**的跨越，重点介绍 **Patsy**（公式 → 设计矩阵）与 **statsmodels**（频率论统计推断、时间序列），并衔接 **scikit-learn**（预测建模）。

**前置**：[第 11 章 时间序列](../chapter11/chapter11_time_series.md) → 本章 → [第 13 章 数据分析案例](../chapter13/chapter13_data_analysis_case_studies.md)。

**本仓库专题**：[`../code/statsmodels/`](../code/statsmodels/)（含 [statsmodels vs sklearn 量化分工](../code/statsmodels/statsmodels_vs_sklearn_quant.md)）

**演示脚本**：[`./code/chapter12_statsmodels_demo.py`](./code/chapter12_statsmodels_demo.py)

---

## 章节总览

**小节统计**（基于当前资料）：2 个一级模块 + 3 个二级小节 + 独立操作块，共 **5 个核心知识块**。

| 一级 | 二级 / 模块 |
|------|-------------|
| 12.1 statsmodels 与 scikit-learn | 量化分工与组合流程（专题见 code/statsmodels/） |
| 12.2 Patsy 模型描述 | 12.2.1 数据转换；12.2.2 分类数据 |
| 12.3 statsmodels | OLS 拟合；12.3.2 时间序列（AutoReg 等） |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [12_01_statsmodels与_scikit_learn_量化分工](./sections/12_01_statsmodels与_scikit_learn_量化分工.md) | statsmodels vs sklearn 核心区别与量化流程（链至专题） |
| [12_02_用_Patsy_创建模型描述](./sections/12_02_用_Patsy_创建模型描述.md) | 用 Patsy 创建模型描述 |
| [12_02_01_用_Patsy_公式进行数据转换](./sections/12_02_01_用_Patsy_公式进行数据转换.md) | 01 用 Patsy 公式进行数据转换 |
| [12_02_02_分类数据和_Patsy](./sections/12_02_02_分类数据和_Patsy.md) | 02 分类数据和 Patsy |
| [12_03_statsmodels_介绍](./sections/12_03_statsmodels_介绍.md) | statsmodels 介绍 |
| [12_03_02_对时间序列过程进行估计](./sections/12_03_02_对时间序列过程进行估计.md) | 02 对时间序列过程进行估计 |

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

见 [`./code/chapter12_statsmodels_demo.py`](./code/chapter12_statsmodels_demo.py)

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
- **scikit-learn**：侧重预测与交叉验证；statsmodels 侧重**推断与诊断**。量化推荐 **先 statsmodels 筛因子，再 sklearn 滚动预测** — 详见 [`../code/statsmodels/statsmodels_vs_sklearn_quant.md`](../code/statsmodels/statsmodels_vs_sklearn_quant.md)。

---

## 本章自检清单

- [ ] 会用 `dmatrices` 理解 y / X 与截距  
- [ ] 知道 `standardize` 的有状态性与 `build_design_matrices`  
- [ ] 会用 `C()` 与交互项 `a:b`  
- [ ] 会用 `smf.ols(...).fit().summary()`  
- [ ] 了解 `AutoReg` 基本用法  
- [ ] 能区分 statsmodels 与 sklearn 在量化中的分工（见 12.1 专题）

---

## 后续扩展留白

（Patsy 高级公式、sklearn Pipeline 与滚动回测框架对接等）
