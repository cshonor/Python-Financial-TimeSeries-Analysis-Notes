# statsmodels vs scikit-learn：股票量化分工与落地流程

> **所属**：[第 12 章](../../chapter12/chapter12_modeling_libraries_patsy_statsmodels.md) · 《利用 Python 进行数据分析》  
> **关联**：[`Using-Python-for-Introductory-Econometrics`](../../../Using-Python-for-Introductory-Econometrics/)（计量推断深化）、[`Python-Time-Series-Forecast`](../../../Python-Time-Series-Forecast/)（滚动预测）

---

## 一、核心定位（一句话区分）

| 库 | 核心 | 输出重点 | 目标 |
|----|------|----------|------|
| **statsmodels** | **统计推断** | 系数、标准误、t 值、p 值、R²、置信区间、异方差/序列相关/F 检验 | **解释**变量关系、验证显著性、因果/归因分析（经典计量） |
| **scikit-learn** | **机器学习预测** | 预测值、MAE/MSE/R²/准确率/AUC 等 | **拟合**数据、泛化预测、特征挖掘（工程化建模） |

**量化记忆**：statsmodels 回答「**这个因子有没有逻辑、稳不稳**」；sklearn 回答「**下一期能不能预测准、信号能不能赚钱**」。

---

## 二、股票量化中的分工

量化常见链路：**因子挖掘 → 模型检验 → 回测建模 → 实盘预测**。两库各司其职、互补使用。

### 2.1 statsmodels：因子检验、归因、风险分析、模型诊断

主打**计量推断**，回答：因子/变量有没有解释力？逻辑是否成立？模型是否可靠？

#### （1）单/多因子有效性检验（截面回归）

截面数据：个股收益率为被解释变量，市值、估值、动量、波动率、财务指标等为解释变量。

```
收益率 = α + β₁·因子1 + β₂·因子2 + ε
```

用 `statsmodels.OLS` / `smf.ols`：

- **p 值**：因子是否统计显著；
- **系数符号**：因子方向（如低 PE 是否超额）；
- **异方差、序列相关检验**：修正标准误，避免假显著；
- **R²**：因子整体解释力度。

> 例：检验「市盈率 PE」能否显著解释个股收益差异——多因子体系最基础的因子筛选。

#### （2）时间序列回归（时序归因、风格分析）

- **风格归因**：个股收益 ~ 大盘 + 行业 + 风格因子；
- **事件研究**：财报/政策公告前后收益变化的统计检验；
- **单位根/协整**：判断价差是否平稳，支撑配对交易、均值回归。

#### （3）风险与残差分析

- 拆解收益残差，识别异常收益；
- 稳健标准误、WLS 修正异方差；
- 面板回归（固定/随机效应）：多股跨期批量检验因子稳定性。

#### （4）受限因变量（涨跌概率推断）

涨跌二元结果 → `Logit` / `Probit`：系数显著性 + 边际效应，**解释**哪些变量在影响涨跌。

---

### 2.2 scikit-learn：特征工程、模型训练、滚动预测、策略回测

主打**预测能力**：有效因子确定后，构建预测模型、生成交易信号。

#### （1）特征加工与筛选

标准化、归一化、缺失填充、编码；方差筛选、RFE 等从海量因子中精简特征。

#### （2）预测模型

- **线性**：`LinearRegression`、`Ridge`、`Lasso`（降维、防过拟合）；
- **树/集成**：`RandomForest`、XGBoost/LightGBM（非线性规律）；
- **分类**：预测涨跌、涨跌档位。

#### （3）样本划分与滚动预测（量化核心）

严禁未来数据泄露：

- 按**时间**划分训练/测试（勿随机 shuffle 时序）；
- **滚动窗口**：每 N 日重训，用最新数据更新参数，预测下一期；
- 预测值 → 交易信号（多/空/持仓）。

#### （4）模型评估

MAE、MSE、Accuracy、AUC；结合回测夏普、最大回撤等——只看「准不准、赚不赚」，不关注系数 p 值。

---

## 三、标准组合流程（两者配合落地）

```
数据清洗 → statsmodels 因子检验筛选 → sklearn 建模预测 → 回测调优
```

### 步骤 1：数据预处理（通用）

获取行情、财务、因子（收盘价、收益率、市值、PE、动量等），清洗、对齐 `(date, code)` 时间轴。

### 步骤 2：statsmodels — 因子筛选 + 逻辑验证

1. 截面/时序 OLS，逐个或批量测试候选因子；
2. 过滤 **p > 0.05** 的不显著因子；
3. 模型诊断：异方差、序列相关；必要时 Newey-West / WLS；
4. 输出**有效因子池**。

> **作用**：剔除噪音因子，保证策略有经济/统计逻辑，避免过拟合幻觉。

### 步骤 3：sklearn — 特征优化 + 预测建模

1. 对有效因子做标准化、降维；
2. 滚动划分训练/测试，训练线性或树模型；
3. 输出下一期收益率 / 涨跌概率；
4. 转化为交易信号。

### 步骤 4：回测与迭代

统计胜率、盈亏比、最大回撤、夏普；效果不佳时回到步骤 2，用 statsmodels 诊断因子失效原因。

---

## 四、场景化案例

### 案例 1：多因子选股（最常用）

| 阶段 | 库 | 做法 |
|------|-----|------|
| 因子检验 | statsmodels | 截面回归 `ret ~ size + pe + momentum + turnover`，看 p 值与系数，剔除无效因子 |
| 预测选股 | sklearn | 有效因子为 X，未来 1 日收益为 y；Lasso/随机森林滚动预测，排序选股 |

### 案例 2：涨跌二分类

| 阶段 | 库 | 做法 |
|------|-----|------|
| 逻辑验证 | statsmodels | Logit：成交量、振幅、均线是否显著影响涨跌 |
| 信号生成 | sklearn | 同特征训练分类器，提升准确率，输出买卖信号 |

### 案例 3：配对交易

| 阶段 | 库 | 做法 |
|------|-----|------|
| 协整检验 | statsmodels | 两股价格协整检验；回归价差与均衡区间 |
| 开平仓 | sklearn | 预测价差走势，判断开仓/平仓时点 |

---

## 五、关键语法速查

### statsmodels

```python
import statsmodels.formula.api as smf

# 截面因子回归（公式 API，推荐）
fit = smf.ols("ret_fwd ~ pe + momentum + C(industry)", data=panel).fit()
print(fit.summary())  # 系数、p 值、R²、F 检验

# 异方差/自相关稳健标准误（时序常用）
fit_hac = fit.get_robustcov_results(cov_type="HAC", maxlags=5)

# 数组 API
import statsmodels.api as sm
X = sm.add_constant(factors)
fit = sm.OLS(y, X).fit()

# Logit 涨跌
fit_logit = smf.logit("up ~ volume + amplitude + ma_gap", data=df).fit()
```

### scikit-learn

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, accuracy_score

# 特征标准化（fit 仅用训练集！）
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)

# 回归预测
model = Lasso(alpha=0.01).fit(X_train_s, y_train)
pred = model.predict(X_test_s)

# 分类
clf = LogisticRegression(max_iter=1000).fit(X_train_s, y_train_bin)
acc = accuracy_score(y_test_bin, clf.predict(X_test_s))
```

### 时序切分（勿用随机 split）

```python
# 按时间切分 — 量化必做
split = int(len(df) * 0.8)
train, test = df.iloc[:split], df.iloc[split:]

# 滚动窗口伪代码
for t in range(window, len(dates)):
    train = panel[panel["date"] < dates[t]]
    test = panel[panel["date"] == dates[t]]
    model.fit(X_train, y_train)
    signal = model.predict(X_test)
```

---

## 六、关键取舍与避坑

| 场景 | 选择 |
|------|------|
| 因子研究、归因、风险拆解、需解释逻辑 | **主要用 statsmodels** |
| 纯黑盒预测、高频、非线性明显、只追收益 | **主要用 sklearn** |
| **量化最优实践** | **先推断，后预测** — 勿直接把一堆因子丢给 sklearn（易过拟合、因子无根） |

**补充细节**：

- statsmodels **也能预测**，但模型族有限，复杂非线性弱；
- sklearn **有系数**，但**无标准误、p 值**，不能做正式统计推断；
- 股票数据常见**异方差、序列相关**，statsmodels 诊断修正是必要环节；
- 截面回归被解释变量用 `shift(-1)` 构造未来收益时，注意**对齐日期、防未来函数**（见第 11 章）。

---

## 七、与全书 / 跨书衔接

| 阶段 | 本书章节 | 衔接 |
|------|----------|------|
| 清洗对齐 | 第 7–8 章 | `dropna`、多表 merge 后再建模 |
| 分组截面 | 第 10 章 | 逐日 `groupby("date").apply(ols)` |
| 时序 | 第 11 章 | `AutoReg`、平稳性、滚动窗口 |
| 推断深化 | Econometrics 册 | OLS 假设、IV、面板、时序计量 |
| 预测深化 | Time-Series 册 | ARIMA、Prophet、深度学习 |

---

## 八、精简背诵版

```
statsmodels → 统计推断 → 因子显著性、模型检验、归因
sklearn     → 预测建模 → 特征工程、滚动训练、信号生成

推荐路线：清洗 → statsmodels 筛因子 → sklearn 预测 → 回测
```

---

## 九、自检

- [ ] 能一句话说清 statsmodels 与 sklearn 的输出差异  
- [ ] 能解释「先推断后预测」为何降低过拟合风险  
- [ ] 知道截面 OLS 与滚动 sklearn 各自在哪一步用  
- [ ] 知道时序数据为何不能 `train_test_split(shuffle=True)`  
- [ ] 能列举 Newey-West / Logit / Lasso 各解决什么问题  

---

## 十、留白

（补充：你的因子池、滚动窗口长度、HAC maxlags 选择、sklearn 模型对比实验记录）

---

[← statsmodels 专题 README](./README.md) · [← 第 12 章](../../chapter12/chapter12_modeling_libraries_patsy_statsmodels.md)
