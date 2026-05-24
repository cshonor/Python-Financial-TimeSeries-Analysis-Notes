# 第 1 章 了解时间序列预测

> 对应教材：**《Python 时间序列预测》** 第 1 章。  
> 全书开篇：时间序列基础概念、**预测项目生命周期**、与常规回归的差异，为后续基线模型、ARIMA/SARIMA、深度学习与 Prophet 打基础。

**前置**（数据处理侧）：[`../Python-Data-Analysis/docs/chapter11_time_series.md`](../Python-Data-Analysis/docs/chapter11_time_series.md)（pandas 时序工具）

**本仓库并行专题**：[`../code/time_series_quant/`](../code/time_series_quant/)（交易日历、resample、rolling、**shift 防前瞻**）

**演示脚本**：[`../code/chapter01_forecast_workflow_demo.py`](../code/chapter01_forecast_workflow_demo.py)

---

## 章节总览

本章介绍时间序列定义、**趋势 / 季节性 / 残差** 分解，以及从目标设定到监控迭代的完整预测工作流；强调时序建模与「可打乱顺序」的回归任务之间的根本差异。

**小节统计**：4 个一级小节 + 嵌套子节，共 **14 个逻辑小节**。

| 一级 | 二级 |
|------|------|
| 1.1 时间序列简介 | — |
| 1.2 时间序列预测概览 | 1.2.1～1.2.8 |
| 1.3 与其他回归的差异 | 1.3.1～1.3.2 |
| 1.4 下一步 / 小结 | — |

---

## 一、书本原文核心知识点提炼

### 1.1 时间序列简介

- **定义**：按时间排序的数据点；常见为**等间隔**（小时、日、月、年）。
- **示例**：股价收盘、用电量、气温等。
- **分解（decomposition）** 三个分量：
  - **趋势（Trend / Level）**：长期缓慢升降。
  - **季节性（Seasonality）**：固定周期内的重复波动（峰、谷）。
  - **残差（Residuals）**：趋势与季节无法解释的随机部分（白噪声）。

### 1.2 时间序列预测概览

完整项目生命周期（数据团队 ↔ 业务价值）：

| 小节 | 要点 |
|------|------|
| 1.2.1 设定目标 | 明确业务目标，证明「为什么要预测」 |
| 1.2.2 确定预测对象 | 预测什么指标（如最低温、销量） |
| 1.2.3 设置预测范围 | 未来一周 / 一月 / 一年 |
| 1.2.4 收集数据 | 历史序列 + 外生变量；**数据量与频率相关**（日频≥1年看年季节；时频数月即可；月/年频需更长历史） |
| 1.2.5 开发模型 | 找趋势/季节；SARIMA、SARIMAX、深度学习等；**时间顺序划分 train/test**，用 MSE 等评估 |
| 1.2.6 部署 | API / 应用等自动出预测 |
| 1.2.7 监控 | 预测 vs 实际；异常事件对精度影响 |
| 1.2.8 收集新数据 | 滚动再训练，保持模型有效 |

### 1.3 时间序列预测与其他回归任务的差异

#### 1.3.1 时间序列有顺序

- **禁止打乱**时间顺序；只能用过去预测未来。
- 训练中使用未来信息 → **前瞻偏差（Look-ahead bias）**，实盘失效。
- 常规 ML 回归常 **shuffle** 增强泛化——时序场景通常**不能**照搬。

#### 1.3.2 时间序列有时没有特征

- 常仅两列：时间戳 + 数值。
- 需用 **MA / AR** 等，仅凭**自身滞后**预测未来（外生变量属扩展，如 SARIMAX）。

### 1.4 下一步（本章小结）

- 后续路径：[第 2 章 基线预测](./chapter02_baseline_forecasting.md) → [第 3 章 随机游走](./chapter03_random_walk.md) → MA/AR → ARIMA/SARIMA/SARIMAX → 深度学习 → **Prophet**。
- **四条戒律**：
  1. 时序 = 按时间排序的点。
  2. 可分解为趋势、季节、残差。
  3. 项目要定目标，部署后要监控。
  4. **建模时绝不打乱时间顺序。**

---

## 二、预测项目生命周期速查

```text
目标 → 预测对象 → 预测 horizon → 收集数据 → 建模与评估 → 部署 → 监控 → 再训练
```

| 阶段 | 交付物 |
|------|--------|
| 定义 | 业务 KPI、预测频率、horizon |
| 数据 | 频率一致、缺失与异常说明 |
| 建模 | 基线 + 至少一种统计/ML 模型；时间切分 test |
| 上线 | 推理接口、版本与回滚 |
| 运维 | 误差监控、漂移、定期重训 |

---

## 三、通用基础示例

见 [`../code/chapter01_forecast_workflow_demo.py`](../code/chapter01_forecast_workflow_demo.py)（合成序列 + 时间切分 + 可选 `seasonal_decompose`）。

---

## 四、【量化专属改造】金融预测工作流

| 书本步骤 | 量化实践 |
|----------|----------|
| 1.2.2 预测对象 | 收益率、波动率、成交量、因子暴露 |
| 1.2.4 数据 | **交易日历**（非自然日）；复权价；[`01_datetime_index_and_trading_calendar.md`](../code/time_series_quant/01_datetime_index_and_trading_calendar.md) |
| 1.2.5 评估 | 滚动/扩展窗口回测；[`04_expanding_window_operations.md`](../code/time_series_quant/04_expanding_window_operations.md) |
| 前瞻偏差 | 信号与标签对齐：[`05_shift_and_signal_alignment.md`](../code/time_series_quant/05_shift_and_signal_alignment.md) |
| 1.2.7 监控 | 实盘预测误差、 regime 变化（波动骤变） |
| 分解 | 价格趋势 + 周内/年内季节；残差作噪声建模 |

---

## 五、与 statsmodels / pandas 的衔接

- **pandas 第 11 章**：`shift`、`resample`、`rolling` 是本章「不准打乱顺序」在代码层的体现。
- **statsmodels.tsa**：后续章节 ARIMA/AutoReg 与本章「仅用滞后预测」一脉相承。
- **评估**：时序 test 取**最后一段**连续时间，不用 `train_test_split(shuffle=True)`。

---

## 本章自检清单

- [ ] 能解释趋势、季节、残差  
- [ ] 能说出预测项目 8 步生命周期  
- [ ] 能说明为何不能 shuffle 时序  
- [ ] 知道数据量与采样频率的关系  
- [ ] 知道后续将学 MA/AR/ARIMA/Prophet 等  

---

## 个人扩展与补充留白

### 1.1

（留白）

### 1.2

（留白）

### 1.3

（留白）

### 1.4

（留白）
