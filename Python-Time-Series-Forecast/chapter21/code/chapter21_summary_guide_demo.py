"""
《Python 时间序列预测》第 21 章配套：全书总结 — 选型与排障速查（无模型训练）

运行：
  python Python-Time-Series-Forecast/code/chapter21_summary_guide_demo.py
"""

from __future__ import annotations

CHAPTER_INDEX = """
=== 全书笔记索引 (ch.1-20) ===
  统计: 1-11  |  DL: 12-18  |  自动: 19-20  |  总结: 21
  README.md 列出每章 .md 与 code/*_demo.py
"""

TOOLKIT = """
=== 21.1 三大兵器库 ===
[统计学]  基线 -> MA/AR -> ARMA -> ARIMA -> SARIMA -> SARIMAX; 多变量 VAR+Granger
          关键: ADF平稳, AIC定阶, 残差白噪声(Ljung-Box)
[深度学习]  >~10k点, 非线性; DataWindow; 线性/DNN/LSTM/CNN/CNN+LSTM/ARLSTM
[自动化]    Prophet: 强季节+假日+长历史; 非银弹(见ch.20弱季节失败)
"""

TROUBLESHOOTING = """
=== 21.2 预测不起作用? 四条排查 ===
1. 本质非时序?     -> 回归分析(外生驱动), 非滞后结构
2. 随机游走?       -> 仅末值/季节基线(ch.3)
3. 粒度过细噪声?   -> resample 到 H/D (ch.18)
4. 单变量不够?     -> SARIMAX外生变量或领域特征(ch.9, ch.20)
"""

OTHER_USES = """
=== 21.3 时序其他应用 ===
分类 | 聚类 | 变点检测 | 仿真 | 信号处理
(本书专注 Forecasting 连续数值预测)
"""

PRACTICE = """
=== 21.4 持续练习数据源 ===
- Papers with Code (Datasets): 时序预测/异常检测 benchmark
- UCI ML Repository: 筛选 Time Series 类型
- Statistics Canada / NYC Open Data (ch.18-20 同类宏观数据)
"""

DECISION = """
=== 快速选型 (业务问答) ===
Q: 数据量?        <500 -> 统计; >10000 -> 考虑DL
Q: 明显季节/假日?  是 -> SARIMA或Prophet; 否 -> 慎Prophet(ch.20)
Q: 多序列因果?     VAR+Granger 或 多输出DL
Q: 有已知X?        SARIMAX 或 DL+特征工程(ch.12)
Q: 要可解释?       统计/Prophet组件图; DL弱
"""


def main() -> None:
    for block in (CHAPTER_INDEX, TOOLKIT, TROUBLESHOOTING, OTHER_USES, PRACTICE, DECISION):
        print(block)
    print("=== 《Python 时间序列预测》全书 21 章学习路径完成 ===")


if __name__ == "__main__":
    main()
