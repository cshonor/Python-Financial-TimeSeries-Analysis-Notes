# 第 19 章 使用 Prophet 自动化时间序列预测

> 对应教材：**《Python 时间序列预测》** 第 19 章。  
> 全书**第四部分（大规模自动化预测）**开篇：引入 Meta **Prophet** — 基于 **加法模型** \(y=g+s+h+\epsilon\)，自动处理趋势、多重季节（傅里叶级数）、节假日；配套 **可视化、交叉验证、超参数调优**。实战：Google Trends **“chocolate”** 月度热度 vs **季节朴素基线** vs **SARIMA**。

**前置**：[第 8 章 SARIMA](./chapter08_sarima_seasonality.md)、[第 18 章 DL 顶点](./chapter18_capstone_household_power.md)

**下一章**：[第 20 章 全书收官顶点](./chapter20_capstone_steak_price.md)（加拿大牛排零售价）

**演示脚本**：[`./code/chapter19_prophet_demo.py`](./code/chapter19_prophet_demo.py)

---

## 章节总览

**小节统计**：7 个一级小节 + 子节，共 **13 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 19.1 | 自动化库生态（Pmdarima / Prophet / NeuralProphet） |
| 19.2 | 加法模型与傅里叶季节 |
| 19.3 | 基础 API：`ds` / `y` |
| 19.4 | 可视化、CV、调参 |
| 19.5 | chocolate 实战 vs SARIMA |
| 19.6～19.7 | 非银弹、练习、小结 |

---

## 一、书本原文核心知识点提炼

### 19.1 自动化预测库概述

- 手动建模耗时长；自动化库加速实验。  
- **Pmdarima**、**Prophet**（Meta，强季节+节假日）、**NeuralProphet**（Prophet + PyTorch）。

**【个人扩展与补充】**  
<br><br><br><br>

### 19.2 探索 Prophet 原理

- 更接近**曲线拟合**，非纯滞后 AR 结构。  
- **\(y(t)=g(t)+s(t)+h(t)+\epsilon_t\)**  
  - \(g(t)\)：趋势（含 changepoints）  
  - \(s(t)\)：年/周/日季节（**傅里叶级数**，年默认 10 项、周 3 项）  
  - \(h(t)\)：节假日  
  - \(\epsilon_t\)：残差  
- **优势**：多季节、缺失与离群鲁棒。

**【个人扩展与补充】**  
<br><br><br><br>

### 19.3 基础工作流

1. `m = Prophet()`  
2. `m.fit(train)` — 列名必须为 **`ds`**, **`y`**  
3. `future = m.make_future_dataframe(periods=365)`  
4. `forecast = m.predict(future)`  
- 核心列：`yhat`, `yhat_lower`, `yhat_upper`（默认 **80%** 区间）  
- 预测曲线通常**平滑**。

**【个人扩展与补充】**  
<br><br><br><br>

### 19.4 高级功能

**19.4.1 可视化**  
- `plot`, `plot_components`, `plot_yearly` / `plot_weekly`  
- `yearly_seasonality` 项数↑ → 更敏感（易过拟合）  
- `add_changepoints_to_plot`

**19.4.2 交叉验证**  
- `cross_validation`：`initial`, `period`, `horizon`  
- `performance_metrics` → MSE / RMSE / MAE

**19.4.3 超参数**  
- `changepoint_prior_scale`（趋势灵活性）  
- `seasonality_prior_scale`（季节强度）  
- 网格搜索 + CV

**【个人扩展与补充】**  
<br><br><br><br>

### 19.5 鲁棒预测实战（chocolate）

**19.5.1 Prophet**  
- 月度数据 → `pd.to_datetime` + **`MonthEnd(1)`** 对齐月末  
- `m.add_country_holidays('US')`  
- 调参后测试集 **MAE = 7.42**；季节基线 **10.92**  
- 组件图：圣诞等假日搜索量**下降**（负向波谷）

**19.5.2 vs SARIMA**  
- 最优 **SARIMA(1,1,1)(1,0,1)₁₂**，MAE **10.09**  
- 优于基线但仍 **逊于 Prophet 7.42**

**【个人扩展与补充】**  
<br><br><br><br>

### 19.6～19.7 下一步、练习、小结

- Prophet **非银弹**：适合**强季节 + 长历史**；须与 SARIMAX/LSTM 等对比。  
- 第 20 章：加拿大牛排价格综合顶点。  
- **小结**：加法模型 + 可视化/CV/调参 → 工业级管线。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | 代码 |
|------|------|
| 初始化 | `Prophet(changepoint_prior_scale=0.05)` |
| 假日 | `m.add_country_holidays('US')` |
| 月末 | `pd.to_datetime(...) + pd.offsets.MonthEnd(1)` |
| CV | `from prophet.diagnostics import cross_validation, performance_metrics` |

---

## 三、演示脚本

见 [`./code/chapter19_prophet_demo.py`](./code/chapter19_prophet_demo.py)

依赖：`pip install prophet pandas statsmodels`（Prophet 建议 Python 3.10–3.12）

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| 业务日频 | `add_country_holidays` + 促销日历 |
| 调参 | 先 CV 粗搜，再固定参数投产 |
| 组合 | Prophet 作基准，DL 作残差修正 |

---

## 五、与全书衔接

| 章 | 关系 |
|----|------|
| 8/11 | SARIMA 手动流程 vs Prophet 自动 |
| 12～18 | DL 手动窗 vs Prophet 开箱 |
| 20 | 综合选型顶点 |

---

## 本章自检清单

- [ ] 能写出加法模型四项  
- [ ] 记住 `ds` / `y` 命名  
- [ ] 能解释 `cross_validation` 三参数  
- [ ] 知道 Prophet 适用场景与局限  

---

## 个人扩展与补充留白

（章节级留白）
