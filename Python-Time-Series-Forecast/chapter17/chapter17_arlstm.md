# 第 17 章 使用预测做出更多预测

> 对应教材：**《Python 时间序列预测》** 第 17 章。  
> 第 16 章多步模型**一次性**输出 24 个点；本章引入 **自回归深度学习（ARLSTM）**：每步预测反馈为下一步输入，可**变长预测**而无需重训。通过自定义 `keras.Model` + **`LSTMCell` / `RNN`** 实现 `warmup` 与 `call` 循环，并讨论 **误差累积** 风险。

**前置**：[第 15 章 LSTM](./chapter15_lstm.md)、[第 16 章 CNN](./chapter16_cnn.md)

**下一章**：[第 18 章 DL 顶点项目](./chapter18_capstone_household_power.md)（家庭用电量）

**演示脚本**：[`./code/chapter17_arlstm_demo.py`](./code/chapter17_arlstm_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 小结，共 **5 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 17.1 | 自回归 vs 固定长度多步 |
| 17.2 | 自定义 ARLSTM 实现与 MAE |
| 17.3 | 工具箱思维 → Prophet / 顶点项目 |
| 17.4 | 练习与小结 |

---

## 一、书本原文核心知识点提炼

### 17.1 研究 ARLSTM 架构

- **传统多步**：网络一次输出固定长度（如 24）；改预测长度需**重开窗 + 重训**。  
- **自回归**：在 \(t\) 输出 \(\hat y_t\)，将 \(\hat y_t\) **反馈**为输入生成 \(t+1\)，循环至目标长度。  
- **优势**：任意长度、多尺度；WaveNet、DeepAR 等均属此类思想。  
- **风险**：**误差累积** — 前期偏差被放大，远期预测变差 → 须严格验证集 / 测试协议。

**【个人扩展与补充】**  
<br><br><br><br>

### 17.2 构建自回归 LSTM 模型

- **数据窗口**：与多步 LSTM 相同 — 输入 **24**、标签 **24**、`shift=24`。  
- **自定义 `AutoRegressive(keras.Model)`**  
  - **`LSTMCell` + `RNN(return_state=True)`**：细粒度状态，便于反馈。  
  - **`warmup`**：整段历史输入 → 首预测 + 初始 `state`。  
  - **`call`**：循环 `out_steps-1` 次，上一步预测 → `lstm_cell` → `Dense` → 堆叠为 `(batch, time, features)`。  
- **MAE（书中测试集）**  
  - **ARLSTM 0.049**  
  - CNN+LSTM **0.055**、LSTM **0.058**、CNN **0.063**  
  - → 本数据集上 **ARLSTM 为多步冠军**。

**【个人扩展与补充】**  
<br><br><br><br>

### 17.3 下一步

- ARLSTM **并非永远最优**；模型均为工具箱选项。  
- 后续：**Prophet**、**牛排价格**等顶点实战。

**【个人扩展与补充】**  
<br><br><br><br>

### 17.4 练习与本章小结

- **练习**：空气质量数据上建 ARLSTM，调 `units`，比 MAE 与 CNN/LSTM。  
- **小结**  
  1. 自回归是 WaveNet、DeepAR 等的基础思想。  
  2. **每步预测反馈**驱动下一步。  
  3. **误差累积**是主要风险。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | API |
|------|------|
| 细粒度 LSTM | `LSTMCell` + `RNN(..., return_state=True)` |
| 自定义模型 | `class AR(keras.Model): def call(self, inputs):` |
| 反馈一步 | `x, state = lstm_cell(x, states=state)` |
| 可变步数 | `out_steps` 循环参数 |

---

## 三、演示脚本

见 [`./code/chapter17_arlstm_demo.py`](./code/chapter17_arlstm_demo.py)

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| 滚动 8/48 步 | 推理时改 `out_steps`，权重复用 |
| 风险控制 | 短 horizon + 定期用真实值重置 |
| 对比 | 仍与一次性多步 LSTM、CNN+LSTM 比 MAE |

---

## 五、与全书衔接

| 章 | 关系 |
|----|------|
| 16 | 一次性多步 vs 自回归多步 |
| 13 | `DataWindow` |
| 18+ | Prophet / 业务顶点 |

---

## 本章自检清单

- [ ] 能对比一次性多步与自回归多步  
- [ ] 能说明误差累积机制  
- [ ] 知道 `LSTMCell` 与 `LSTM` 层区别  
- [ ] 能解释 `warmup` 与 `call` 分工  

---

## 个人扩展与补充留白

（章节级留白）
