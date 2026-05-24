# 第 14 章 初步研究深度学习

> 对应教材：**《Python 时间序列预测》** 第 14 章。  
> 在 [第 13 章 `DataWindow` 与基线](./chapter13_data_window_baselines.md) 之上，本章搭建可训练架构：**线性模型**（无隐藏层）与 **DNN**（ReLU 隐藏层）。在 **单步 / 多步 / 多输出** 三种场景下用 **MAE** 对比基线、线性与 DNN，说明 DNN 能拟合**非线性**关系。

**前置**：第 12 章预处理、第 13 章数据窗口

**下一章**：[第 15 章 LSTM](./chapter15_lstm.md)（序列记忆）

**演示脚本**：[`../code/chapter14_linear_dnn_demo.py`](../code/chapter14_linear_dnn_demo.py)  
**依赖**：`pip install tensorflow`（建议 Python 3.10–3.12）；无 TF 时演示脚本用 **sklearn** 回退对比线性 vs MLP

---

## 章节总览

**小节统计**：4 个一级小节 + 14.1/14.2 各 3 子节 + 小结，共 **11 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 14.1 | 线性模型 + `compile_and_fit` |
| 14.2 | DNN（64×2 + ReLU） |
| 14.3 | 引出 LSTM |
| 14.4 | 练习与小结 |

---

## 一、书本原文核心知识点提炼

### 14.1 实现线性模型

- **本质**：无隐藏层，等价多元线性回归；各特征加权求和。  
- **`compile_and_fit`**：`loss='mse'`、`optimizer='adam'`、`metrics=['mae']`；**EarlyStopping** `patience=3` 防过拟合。

**14.1.1 单步**：`Sequential` → `Dense(units=1)`，预测下一时刻流量。  

**14.1.2 多步**：输入 24h → 输出 24h；书中用 `Dense(1)` 常配合 **TimeDistributed** 或展平后映射到 24 维；`kernel_initializer=zeros` 可加速收敛。  

**14.1.3 多输出**：`Dense(units=2)` 同时预测流量与温度。

**【个人扩展与补充】**  
<br><br><br><br>

### 14.2 实现深度神经网络 (DNN)

- **隐藏层**：全连接之间插入 **2 的幂** 单元（如 **64**）。  
- **ReLU**：\(f(x)=\max(0,x)\)，梯度与计算友好，隐藏层首选。  
- **单步 DNN**：`Dense(64, relu)` × 2 → `Dense(1)`。  
- **多步 / 多输出**：同样两层 64-ReLU；输出 `Dense(24)` 或 `Dense(2)` / `TimeDistributed`。  
- **结果**：各场景 **DNN MAE 最小** > 线性 > 基线。

**【个人扩展与补充】**  
<br><br><br><br>

### 14.3 下一步

- Dense 网络难以显式利用**时间顺序与记忆** → 第 15 章 **LSTM**。

**【个人扩展与补充】**  
<br><br><br><br>

### 14.4 练习与本章小结

- **练习**：第 13 章空气质量数据上重做线性 + DNN，调层宽/层数。  
- **小结**  
  1. 线性模型**只能**线性关系。  
  2. DNN 增加隐藏层，通常显著改进。  
  3. 隐藏层须 **非线性激活**（ReLU 等）。  
  4. 隐藏单元数宜为 **2 的幂**。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | Keras |
|------|-------|
| 编译 | `model.compile(optimizer='adam', loss='mse', metrics=['mae'])` |
| 早停 | `EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)` |
| 单步线性 | `Flatten` → `Dense(1)` |
| DNN | `Dense(64, activation='relu')` × 2 |
| 多步 | `Flatten` → `Dense(24)` 或 `TimeDistributed(Dense(1))` |

---

## 三、演示脚本

见 [`../code/chapter14_linear_dnn_demo.py`](../code/chapter14_linear_dnn_demo.py)

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| 因子+价量 | 多特征输入 `Dense`；注意标准化 |
| 调参 | `units`、层数、`patience`、`learning_rate` |
| 上线 | 验证集 MAE 须稳定低于基线 |

---

## 五、与全书衔接

| 章 | 关系 |
|----|------|
| 13 | 基线 MAE 标尺 |
| 15 | LSTM 替代纯 Dense 序列建模 |
| 6 | MSE/MAE 与统计篇一致 |

---

## 本章自检清单

- [ ] 能写出 `compile_and_fit` 三要素  
- [ ] 能说明线性 vs DNN 结构差异  
- [ ] 知道 ReLU 的作用  
- [ ] 能读验证集 MAE 对比表  

---

## 个人扩展与补充留白

（章节级留白）
