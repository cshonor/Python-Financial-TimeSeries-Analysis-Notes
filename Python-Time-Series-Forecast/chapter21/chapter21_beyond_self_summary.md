# 第 21 章 超越自我（全书总结与展望）

> 对应教材：**《Python 时间序列预测》** 第 21 章 · **全书终章**。  
> 系统复盘 **统计学 / 深度学习 / 自动化（Prophet）** 三大体系的使用边界，给出预测失效时的**排障指南**，并介绍时序在**分类、聚类、变点检测**等方向的应用与**开源数据集**资源。

**前置**：第 1～20 章全书主线

**配套**：[`./code/chapter21_summary_guide_demo.py`](./code/chapter21_summary_guide_demo.py)（选型与排障速查，无新模型训练）

---

## 章节总览

| 小节 | 主题 |
|------|------|
| 21.1 | 三大兵器库总结（含 21.1.1～21.1.3） |
| 21.2 | 预测不起作用怎么办 |
| 21.3 | 时序的其他应用 |
| 21.4 | 保持练习 |

---

## 一、书本原文核心知识点提炼

### 21.1 总结所学

**21.1.1 统计学预测**

| 层级 | 内容 |
|------|------|
| 起点 | 基线（末值、季节朴素） |
| 核心 | MA(q)、AR(p) → ARMA → ARIMA → **SARIMA** → **SARIMAX** |
| 多变量 | **VAR(p)** + **Granger** 双向检验 |
| 铁律 | **ADF 平稳** → **AIC 定阶** → **残差白噪声**（Ljung-Box） |
| 顶点 | [第 11 章](./chapter11_capstone_aus_drugs.md) |

**21.1.2 深度学习预测**

| 条件 | 数据 **>~10,000** 点、强非线性、高维特征 |
|------|------|
| 基础 | 线性 → **DNN**（ReLU 隐藏层） |
| 序列 | **LSTM** 记忆；**CNN** 滤噪、训练快 |
| 进阶 | **CNN+LSTM**、**ARLSTM**（反馈预测，DeepAR 思想） |
| 基石 | [第 13 章](./chapter13_data_window_baselines.md) **DataWindow** |
| 顶点 | [第 18 章](./chapter18_capstone_household_power.md) |

**21.1.3 自动化预测（Prophet）**

- 加法模型 \(y=g+s+h+\epsilon\)；多重季节、假日、changepoints。  
- **优点**：快速、内置 CV、鲁棒。  
- **局限**：控制力弱；**强季节 + 长历史** 最合适（[第 19 章](./chapter19_prophet.md) chocolate）。  
- **反例**：[第 20 章](./chapter20_capstone_steak_price.md) 弱季节 → Prophet 输给基线。

**【个人扩展与补充】**  
<br><br><br><br>

### 21.2 如果预测不起作用怎么办

1. **不是时序问题** → 用**回归**（\(y\) 由广告支出等驱动，非时间本身）。  
2. **随机游走** → 只能**末值基线**（[第 3 章](./chapter03_random_walk.md)）。  
3. **粒度太细** → **重采样**（分钟→小时/天）（[第 18 章](./chapter18_capstone_household_power.md)）。  
4. **单变量枯竭** → **外生变量** + 领域知识（[第 9 章 SARIMAX](./chapter09_sarimax_exogenous.md)、第 20 章）。

**【个人扩展与补充】**  
<br><br><br><br>

### 21.3 时间序列数据的其他应用

本书聚焦 **Forecasting（预测连续数值）**。  
其他方向：**分类、聚类、变点检测、仿真、信号处理**。

**【个人扩展与补充】**  
<br><br><br><br>

### 21.4 保持练习

- 持续用**新数据**试错。  
- **Papers with Code (Datasets)**：近百套时序任务数据。  
- **UCI ML Repository**：筛选 “Time Series” 类型。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、全书路线图（1～20 章）

```text
Part I–II  统计：1基线 → 3RW → 4MA → 5AR → 6ARMA → 7ARIMA → 8SARIMA
           → 9SARIMAX → 10VAR → 11统计顶点
Part III   DL：12预处理 → 13窗口/基线 → 14线性/DNN → 15LSTM → 16CNN
           → 17ARLSTM → 18DL顶点
Part IV    自动：19Prophet → 20收官顶点（牛排）
Part V     21总结（本章）
```

---

## 三、选型决策速查（量化场景）

| 场景 | 优先考虑 |
|------|----------|
| 样本 < 数百、需可解释 | SARIMA / SARIMAX |
| 双向宏观变量 | VAR + Granger |
| >1 万点、非线性 | DL（LSTM/CNN/ARLSTM） |
| 强季节 + 假日、快速上线 | Prophet |
| 弱季节、仅趋势 | 基线或 SARIMAX，慎用 Prophet |
| 多因子已知 | SARIMAX 或 DL 多特征 |

运行 [`chapter21_summary_guide_demo.py`](./code/chapter21_summary_guide_demo.py) 可打印交互式检查清单。

---

## 四、全书自检（毕业清单）

- [ ] 能画出三大体系适用边界  
- [ ] 能独立完成：ADF → AIC → 残差 → 滚动评估  
- [ ] 能配置 DataWindow 与 DL 基线  
- [ ] 知道 Prophet 何时会失败  
- [ ] 预测失效时能按 21.2 四条排查  

---

## 个人扩展与补充留白

（全书毕业留白）
