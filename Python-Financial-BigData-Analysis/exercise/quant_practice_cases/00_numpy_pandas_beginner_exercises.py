"""
NumPy & Pandas 量化新手练习清单（可直接运行）

用法：
  python Pandas/05_quant_practice_cases/00_numpy_pandas_beginner_exercises.py

说明：
  - 每个练习对应一个函数：numpy_01 ~ numpy_04, pandas_01 ~ pandas_06
  - 默认按顺序全部跑完；你也可以在 main() 里只跑某几个
"""

from __future__ import annotations


def numpy_01_simulate_ohlc_basic_calcs() -> None:
    """练习 1：用 NumPy 模拟 K 线数据并做基础计算"""
    import numpy as np

    print("\n========== NumPy 练习 1：模拟收盘价 + 基础统计 + 5日均线 ==========")

    np.random.seed(42)
    close = np.random.normal(loc=100, scale=2, size=100)

    returns = np.diff(close) / close[:-1]
    print("日收益率均值：", returns.mean())
    print("日收益率标准差：", returns.std())
    print("单日最大涨幅：", returns.max())
    print("单日最大跌幅：", returns.min())

    window = 5
    ma5 = np.convolve(close, np.ones(window) / window, mode="valid")
    print("5日均线长度：", len(ma5))


def numpy_02_vectorized_signal_cross() -> None:
    """练习 2：NumPy 向量化实现一个简单策略信号（上穿/下穿）"""
    import numpy as np

    print("\n========== NumPy 练习 2：向量化金叉/死叉信号 ==========")

    np.random.seed(42)
    close = np.random.normal(100, 2, 100)
    ma20 = np.convolve(close, np.ones(20) / 20, mode="same")

    cross_up = (close[1:] > ma20[1:]) & (close[:-1] <= ma20[:-1])
    cross_down = (close[1:] < ma20[1:]) & (close[:-1] >= ma20[:-1])

    print("金叉发生的位置：", np.where(cross_up)[0])
    print("死叉发生的位置：", np.where(cross_down)[0])


def numpy_03_simple_backtest_array_logic() -> None:
    """练习 3：NumPy 实现简单的回测逻辑（position × return）"""
    import numpy as np

    print("\n========== NumPy 练习 3：数组回测逻辑（持仓×收益） ==========")

    np.random.seed(42)
    close = np.random.normal(100, 2, 100)
    position = np.zeros(len(close))
    position[20:50] = 1

    daily_returns = np.diff(close) / close[:-1]
    strategy_returns = daily_returns * position[:-1]

    cumulative_returns = np.cumprod(1 + strategy_returns)
    print("策略累计收益：", cumulative_returns[-1])


def numpy_04_risk_metrics_sharpe_mdd() -> None:
    """练习 4：NumPy 统计分析（夏普 / 最大回撤）"""
    import numpy as np

    print("\n========== NumPy 练习 4：夏普比率 + 最大回撤 ==========")

    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 1000)

    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252)
    print("夏普比率：", sharpe_ratio)

    cumulative = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()
    print("最大回撤：", max_drawdown)


def pandas_01_build_kline_dataframe() -> "tuple[object, object]":
    """练习 1：从无到有构建一份标准 K 线 DataFrame"""
    import numpy as np
    import pandas as pd

    print("\n========== Pandas 练习 1：构建 K 线 DataFrame（OHLCV + 时间索引） ==========")

    dates = pd.date_range(start="2025-01-01", periods=100, freq="D")

    np.random.seed(42)
    data = {
        "open": np.random.normal(100, 2, 100),
        "high": np.random.normal(101, 2, 100),
        "low": np.random.normal(99, 2, 100),
        "close": np.random.normal(100, 2, 100),
        "volume": np.random.randint(1000, 5000, 100),
    }
    df = pd.DataFrame(data, index=dates)

    print(df.head())
    print("索引类型：", type(df.index))
    return df, pd


def pandas_02_basic_indicators(df, pd_module) -> None:
    """练习 2：收益率、均线、波动率"""
    import numpy as np

    pd = pd_module
    print("\n========== Pandas 练习 2：收益率 + 均线 + 波动率 ==========")

    df["return"] = df["close"].pct_change()
    df["ma5"] = df["close"].rolling(5).mean()
    df["ma20"] = df["close"].rolling(20).mean()
    df["volatility_20"] = df["return"].rolling(20).std() * np.sqrt(252)

    print(df[["close", "return", "ma5", "ma20"]].tail())


def pandas_03_signal_and_shift_alignment(df, pd_module) -> None:
    """练习 3：信号生成 + shift(1) 对齐（避免未来函数）"""
    pd = pd_module
    print("\n========== Pandas 练习 3：信号 + shift 对齐（避免未来函数） ==========")

    df["signal"] = 0
    df.loc[df["ma5"] > df["ma20"], "signal"] = 1
    df.loc[df["ma5"] < df["ma20"], "signal"] = 0

    df["position"] = df["signal"].shift(1)
    df["strategy_return"] = df["return"] * df["position"]

    print(df[["close", "ma5", "ma20", "signal", "position", "strategy_return"]].tail(10))


def pandas_04_missing_and_outlier_handling(pd_module) -> None:
    """练习 4：缺失值 & 异常值处理"""
    import numpy as np
    import pandas as pd

    print("\n========== Pandas 练习 4：缺失值 + 异常值清洗 ==========")

    dates = pd.date_range("2025-01-01", periods=10, freq="D")
    data = {"close": [100, 101, np.nan, 103, 200, 105, np.nan, 107, 108, 109]}
    df = pd.DataFrame(data, index=dates)

    df["close_ffill"] = df["close"].fillna(method="ffill")
    df["return"] = df["close_ffill"].pct_change()
    df["return_clean"] = df["return"].clip(-0.1, 0.1)

    print(df)


def pandas_05_groupby_multi_stock(pd_module) -> None:
    """练习 5：groupby 分组（多股票回测基础）"""
    import numpy as np
    import pandas as pd

    print("\n========== Pandas 练习 5：多股票 groupby（每股收益 + 等权组合） ==========")

    dates = pd.date_range("2025-01-01", periods=10, freq="D")
    stocks = ["AAPL", "MSFT", "GOOG"]

    np.random.seed(42)
    data = []
    for stock in stocks:
        for date in dates:
            data.append({"date": date, "stock": stock, "close": np.random.normal(100, 2)})
    df = pd.DataFrame(data)

    df["return"] = df.groupby("stock")["close"].pct_change()
    daily_return = df.groupby("date")["return"].mean()
    print("每日等权收益：\n", daily_return)


def pandas_06_merge_price_and_factor(pd_module) -> None:
    """练习 6：merge 合并数据（行情 + 因子）"""
    import pandas as pd

    print("\n========== Pandas 练习 6：merge 合并（行情 + 因子） ==========")

    dates = pd.date_range("2025-01-01", periods=5, freq="D")
    price_data = pd.DataFrame({"date": dates, "close": [100, 101, 102, 103, 104]})
    factor_data = pd.DataFrame(
        {"date": dates, "momentum": [0.01, 0.02, -0.01, 0.03, 0.005]}
    )

    merged = pd.merge(price_data, factor_data, on="date", how="left")
    print(merged)


def main() -> None:
    numpy_01_simulate_ohlc_basic_calcs()
    numpy_02_vectorized_signal_cross()
    numpy_03_simple_backtest_array_logic()
    numpy_04_risk_metrics_sharpe_mdd()

    try:
        df, pd_module = pandas_01_build_kline_dataframe()
        pandas_02_basic_indicators(df, pd_module)
        pandas_03_signal_and_shift_alignment(df, pd_module)
        pandas_04_missing_and_outlier_handling(pd_module)
        pandas_05_groupby_multi_stock(pd_module)
        pandas_06_merge_price_and_factor(pd_module)
    except ModuleNotFoundError as e:
        # 你的环境若未安装 pandas，会在这里提示；脚本本身不报错退出
        print("\n[提示] 未安装依赖，Pandas 部分未执行：", e)
        print("你可以先安装：pip install pandas numpy")


if __name__ == "__main__":
    main()

