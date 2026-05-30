# 第 4 章 移动平均过程建模

> 对应教材：**《Python 时间序列预测》** 第 4 章。  
> 第 3 章随机游走之后，本章引入第一种可学习的统计模型：**移动平均过程 MA(q)**。内容含 MA 定义、用 **ACF 定阶**、预测步长 ≤ \(q\) 的限制、**滚动预测**，以及差分后的 **逆变换** 完整流程。

**前置**：[第 3 章 随机游走](./chapter03_random_walk.md)（ADF、ACF、差分）

**下一章**：[第 5 章 自回归 AR(p)](./chapter05_autoregressive_process.md)（ACF 缓慢衰减时用 PACF 定阶）

**演示脚本**：[`./code/chapter04_ma_process_demo.py`](./code/chapter04_ma_process_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 4.4 含 2 子节 + 本章小结，共 **7 个逻辑小节**。

| 一级 | 内容 |
|------|------|
| 4.1 定义 MA 过程 | 公式、定阶、ACF 截断 |
| 4.2 预测 MA 过程 | 步长限制、滚动预测、SARIMAX、逆变换 |
| 4.3 下一步 | 引出 AR / PACF |
| 4.4 练习 | ArmaProcess 模拟、端到端 |

---

## 一、书本原文核心知识点提炼

### 4.1 定义移动平均过程

- **MA(q)**：\(y_t = \mu + \epsilon_t + \theta_1\epsilon_{t-1} + \cdots + \theta_q\epsilon_{t-q}\)。
- \(\epsilon_t\)：相互独立、常设正态（白噪声）；\(\theta_i\) 为过去误差权重。
- **阶数 \(q\)**：依赖过去 \(q\) 个误差；MA(1) 仅 \(\epsilon_{t-1}\)，MA(2) 至 \(\epsilon_{t-2}\)。

**识别步骤**：

1. **ADF** → 不平稳则差分/变换至平稳。  
2. 画平稳序列 **ACF**。  
3. **截断**：lag \(1..q\) 显著，**\(q+1\) 起落入置信带** → 定为 MA(q)。

### 4.2 预测移动平均过程

- **硬限制**：MA(q) **不能直接预测超过 \(q\) 步**；更远步长未来误差未观测，预测退化为 **\(\mu\)**。
- **滚动预测（Rolling Forecast）**：以 ≤\(q\) 步为窗口，在测试集上反复拟合/预测并前移，覆盖长 horizon。
- **实现**：`statsmodels` 用 **`SARIMAX(..., order=(0, 0, q))`**（无 AR、无差分、无季节）拟合 MA(q)。
- **逆变换**：在**差分平稳**序列上训练 → 预测为差分值；一阶差分还原：**`cumsum()` + 测试前最后一个水平值 \(y_0\)**。
- **评估**：逆变换后与实测比 **MSE/MAE**，须优于 [第 2 章](./chapter02_baseline_forecasting.md) 基线。

### 4.3 下一步

- ACF 在 \(q\) 处截断 → MA。  
- ACF **缓慢衰减** 或 **正弦式** 波动 → **非 MA**，用 **PACF** 定 AR 阶 → [第 5 章](./chapter05_autoregressive_process.md)。

### 4.4 练习与本章小结

- **`statsmodels.tsa.arima_process.ArmaProcess`** 模拟 MA(2) 等。  
- 端到端：ADF → ACF 定 \(q\) → 划分 → 滚动预测 → MSE。

**小结四条**：

1. 当前值依赖 \(\mu\)、当前与过去 \(\epsilon\)。  
2. ACF 定 \(q\)。  
3. 直接预测 ≤\(q\) 步；更长用滚动预测。  
4. 训练在平稳（常差分）序列上，预测须 **逆变换** 回原尺度。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 模拟 MA | `ArmaProcess(ar=[1], ma=[1, θ1, θ2]).generate_sample(n)` |
| 拟合 MA(q) | `SARIMAX(y, order=(0,0,q)).fit()` |
| 短期预测 | `res.forecast(steps=q)` |
| 滚动预测 | 循环：扩展训练 → `fit` → `forecast(steps≤q)` |
| 差分还原 | `y0 + diff_forecast.cumsum()` |
| ACF 定阶 | `plot_acf(y_stationary)` |

---

## 三、通用基础示例

见 [`./code/chapter04_ma_process_demo.py`](./code/chapter04_ma_process_demo.py)

---

## 四、【量化专属改造】金融 MA 建模

| 要点 | 实践 |
|------|------|
| 对象序列 | 常对 **收益率**（已近似平稳）拟合 MA；对价格先差分 |
| 阶数 \(q\) | 日频 \(q\) 通常很小；用 AIC/BIC 与 ACF 交叉验证 |
| 预测 horizon | 日频多步需滚动；勿对 MA(1) 一次 `forecast(20)` |
| 与基线比 | 样本外 MSE 须低于季节朴素 / 末值（第 2、3 章） |
| 滚动窗口 | 与 [`03_rolling_window_operations.md`](../../code/time_series_quant/03_rolling_window_operations.md) 思想一致，但此处是**模型重拟合** |

---

## 五、与全书衔接

- **第 2 章**：MA 模型须证明优于 MAPE 基线。  
- **第 3 章**：纯 RW 无 MA 结构；差分白噪声才谈 MA(q)。  
- **pandas 第 11 章**：`diff`、`cumsum` 对应差分与逆变换。  
- **statsmodels**：`SARIMAX` 后续扩展为 ARMA、ARIMA、SARIMA。

---

## 本章自检清单

- [ ] 能写出 MA(q) 公式  
- [ ] 会用 ACF「截断」判断 \(q\)  
- [ ] 理解为何只能直接预测 \(q\) 步  
- [ ] 会用 `order=(0,0,q)` 拟合  
- [ ] 会对差分预测做 `cumsum` 还原  

---

## 个人扩展与补充留白

### 4.1～4.4

（留白）
