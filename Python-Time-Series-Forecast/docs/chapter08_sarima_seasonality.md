# 第 8 章 考虑季节性

> 对应教材：**《Python 时间序列预测》** 第 8 章。  
> 在 **ARIMA(p,d,q)**（第 7 章）之上引入季节性：**SARIMA(p,d,q)(P,D,Q)\_m**。本章讲解季节性参数、**STL 分解**识别季节、升级后的 AIC 网格工作流，并以航空月度客流对比 ARIMA 与 SARIMA。

**前置**：[第 6 章 ARMA](./chapter06_arma_modeling.md) → [第 7 章 ARIMA](./chapter07_arima_nonstationary.md)

**下一章**：[第 9 章 SARIMAX](./chapter09_sarimax_exogenous.md)（外生变量 X）

**演示脚本**：[`../code/chapter08_sarima_demo.py`](../code/chapter08_sarima_demo.py)

---

## 章节总览

**小节统计**：5 个一级小节 + 8.3 含 2 子节 + 小结，共 **8 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 8.1 | SARIMA 参数 \(P,D,Q,m\) |
| 8.2 | 识别季节性：折线图、STL |
| 8.3 | 航空乘客：ARIMA vs SARIMA |
| 8.4 | 引出 SARIMAX |
| 8.5 | 练习与小结 |

---

## 一、书本原文核心知识点提炼

### 8.1 研究 SARIMA(p,d,q)(P,D,Q)m

- **定义**：ARIMA + 季节性参数；\(P=D=Q=0\) 时退化为 ARIMA。
- **\(P,D,Q\)**：季节性 AR、季节差分、季节 MA 阶数。
- **\(m\)**：一完整季节周期内的观测数  
  - 月频年季节：**\(m=12\)**；季频：**\(m=4\)**；周频年季节：**\(m=52\)**  
  - 日频：周季节 \(m=7\)，年季节 \(m=365\)；时频：日 \(m=24\)，周 \(m=168\)
- **预测逻辑**：用滞后 \(m, 2m, \ldots\) 的观测（如往年同月）作预测因子。

### 8.2 识别季节性模式

- **折线图**：重复峰谷（如每年夏高峰）。
- **STL 分解**：趋势 + **季节** + 残差；`STL(y, period=m)`。  
  - 季节分量近 **0 水平线** → 可不用 SARIMA。  
  - 图解法足够决定是否上 SARIMA。

### 8.3 预测航空公司每月乘客数量

**升级后的通用流程**：记录 **\(d\)** 与 **\(D\)**（季节差分次数）；网格同时搜 **\(p,q,P,Q\)**，AIC 最小 + Ljung-Box。

#### 8.3.1 ARIMA 对照（无季节）

- 两次普通差分平稳：\(d=2, D=0\)；最优例 **ARIMA(11,2,3)**。
- Ljung-Box **前两阶 \(p<0.05\)** → 残差仍相关 → **漏掉季节信息**。

#### 8.3.2 SARIMA

- 月数据 **\(m=12\)**；\(d=1, D=1\)（一阶 + 季节一阶差分）后 ADF 平稳。
- 最优例：**SARIMA(2,1,1)(1,1,2)\_12**；Ljung-Box **全 \(p>0.05\)**。
- **MAE**：季节朴素 **10.92** > ARIMA **3.85** > **SARIMA 2.85**。

### 8.4 下一步

- 脉络：MA/AR → ARMA → ARIMA → **SARIMA**。  
- SARIMA 只用**自身滞后**；外生变量 → [第 9 章 SARIMAX](./chapter09_sarimax_exogenous.md)。

### 8.5 练习与小结

1. SARIMA 在 ARIMA 上增加 \((P,D,Q)_m\)。  
2. **\(m\)** = 每周期观测数。  
3. **STL** 识别季节。  
4. 有季节时 ARIMA 残差常未白噪声；SARIMA 更优。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| SARIMA 拟合 | `SARIMAX(y, order=(p,d,q), seasonal_order=(P,D,Q,m))` |
| STL | `STL(y, period=12, robust=True).fit()` |
| 季节差分 | `y.diff(12)` 或模型内 \(D=1\) |
| AIC 网格 | 遍历 `(p,d,q)` × `(P,D,Q)` |
| 残差 | `acorr_ljungbox(res.resid)`，\(p>0.05\) |
| 季节基线 | 重复最近 12 个月（[第 2 章](./chapter02_baseline_forecasting.md)） |

---

## 三、通用基础示例

见 [`../code/chapter08_sarima_demo.py`](../code/chapter08_sarima_demo.py)

---

## 四、【量化专属改造】金融季节性

| 场景 | \(m\) 示例 |
|------|-----------|
| 月频盈利/宏观 | 12（年季节） |
| 季频财报 | 4 |
| 日频 A 股 | 5（周）或 252（年，近似） |
| 5 分钟线 | 48（日）或按日历自定义 |

- 春节、财报披露 → 除 SARIMA 外常需 **SARIMAX 哑变量**（第 9 章）。  
- 对比：样本外 MAE 须击败 [第 2 章](./chapter02_baseline_forecasting.md) **季节朴素**。

---

## 五、与全书衔接

| 章 | 衔接 |
|----|------|
| 1 | 分解 = 趋势/季节/残差 |
| 2 | 季节朴素 MAPE 基线 |
| 6 | AIC + Ljung-Box 工作流 |
| 7 | ARIMA = SARIMA 当 \(P=D=Q=0\) |
| 11 (pandas) | `period=12` 重采样对齐 |

---

## 本章自检清单

- [ ] 能解释 \(m, P, D, Q\)  
- [ ] 会用 STL 看季节分量  
- [ ] 会写 `seasonal_order=(P,D,Q,m)`  
- [ ] 能说明 ARIMA 在季节数据上 LB 失败的原因  
- [ ] 知道 SARIMAX 是下一章方向  

---

## 个人扩展与补充留白

### 8.1～8.5

（留白）
