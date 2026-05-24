import numpy as np
import pandas as pd


def make_price_data(n: int = 60, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2025-01-01", periods=n)  # 用工作日近似交易日

    ret = rng.normal(loc=0.0005, scale=0.01, size=n)
    close = 100 * (1 + pd.Series(ret, index=dates)).cumprod()
    open_ = close.shift(1).fillna(close.iloc[0]) * (1 + rng.normal(0, 0.002, size=n))
    high = np.maximum(open_, close) * (1 + rng.uniform(0, 0.005, size=n))
    low = np.minimum(open_, close) * (1 - rng.uniform(0, 0.005, size=n))
    volume = rng.integers(800, 2000, size=n)

    df = pd.DataFrame(
        {
            "open": open_.to_numpy(),
            "high": high.to_numpy(),
            "low": low.to_numpy(),
            "close": close.to_numpy(),
            "volume": volume,
        },
        index=dates,
    )
    df.index.name = "date"
    return df.sort_index()


def make_factor_data(dates: pd.DatetimeIndex, seed: int = 13) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    factor = rng.normal(0, 1, size=len(dates))
    df = pd.DataFrame({"date": dates, "factor": factor})

    # 制造缺失，模拟因子数据断档
    miss_idx = rng.choice(len(dates), size=max(3, len(dates) // 12), replace=False)
    df.loc[miss_idx, "factor"] = np.nan
    return df


def make_multi_asset_long(dates: pd.DatetimeIndex, seed: int = 21) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    codes = ["000001", "000002", "000003"]
    rows: list[dict] = []

    for code in codes:
        # 每只股票独立的随机过程
        ret = rng.normal(loc=0.0003, scale=0.012, size=len(dates))
        close = 50 * (1 + pd.Series(ret, index=dates)).cumprod()
        factor = rng.normal(0, 1, size=len(dates))
        for d, c, f in zip(dates, close.to_numpy(), factor):
            rows.append({"date": d, "code": code, "close": float(c), "factor": float(f)})

    return pd.DataFrame(rows).sort_values(["date", "code"]).reset_index(drop=True)


def main() -> None:
    print("\n===== 0) 构造数据 =====")
    df_price = make_price_data(n=60)
    print(df_price.head())

    df_factor = make_factor_data(df_price.index)
    print("\nFactor raw (with NaN):")
    print(df_factor.head(10))

    print("\n===== 1) 选：筛选 / 取列 / 条件 =====")
    # 取列
    print(df_price[["open", "close"]].head(3))

    # 条件过滤：阳线
    bullish = df_price[df_price["close"] > df_price["open"]]
    print("\nBullish days:", len(bullish))

    # 最近 20 天
    last_20 = df_price.tail(20)
    print("\nLast 20 rows:", last_20.shape)

    print("\n===== 2) 改：新增列 / 缺失值 / 类型 =====")
    df = df_price.copy()
    df["ret"] = df["close"].pct_change()
    df["ret_clipped"] = df["ret"].clip(-0.2, 0.2)

    # 合并因子前：先把 factor 的 date 转成索引，并 ffill（常见：低频/缺失因子对齐到交易日）
    factor = df_factor.copy()
    factor = factor.set_index("date").sort_index()
    factor["factor_ffill"] = factor["factor"].ffill()
    print(factor.head(10))

    print("\n===== 4) 拼：merge 合并 + 校验 =====")
    df_merged = pd.merge(
        df.reset_index(),
        factor[["factor_ffill"]].reset_index(),
        on="date",
        how="left",
        validate="one_to_one",
    ).set_index("date")
    print(df_merged[["close", "ret", "factor_ffill"]].head())
    print("\nMissing after merge:")
    print(df_merged[["factor_ffill"]].isna().sum())

    print("\n===== 3) 算：rolling / signal / shift 对齐 =====")
    df_merged["ma20"] = df_merged["close"].rolling(20, min_periods=20).mean()
    df_merged["vol20"] = df_merged["ret"].rolling(20, min_periods=20).std()

    # 简单信号：close > ma20 为 1，否则 0；执行信号必须 shift(1) 避免未来函数
    raw_signal = (df_merged["close"] > df_merged["ma20"]).astype(int)
    df_merged["signal"] = raw_signal.shift(1).fillna(0).astype(int)

    df_merged["strategy_ret"] = df_merged["signal"] * df_merged["ret"]
    df_merged["strategy_cum"] = (1 + df_merged["strategy_ret"].fillna(0)).cumprod()
    df_merged["bench_cum"] = (1 + df_merged["ret"].fillna(0)).cumprod()

    print(df_merged[["close", "ma20", "signal", "strategy_cum", "bench_cum"]].tail(5))

    print("\n===== 加餐：多资产长表的 groupby（按 code 独立计算） =====")
    df_multi = make_multi_asset_long(df_price.index)
    df_multi["ret"] = df_multi.groupby("code")["close"].pct_change()

    # 截面排名：每天对 factor 排名，选前 20%
    df_multi["factor_rank"] = df_multi.groupby("date")["factor"].rank(pct=True)
    df_multi["selected"] = (df_multi["factor_rank"] >= 0.8).astype(int)

    # 次日执行（按 code shift）
    df_multi["selected_lag1"] = df_multi.groupby("code")["selected"].shift(1).fillna(0).astype(int)

    # 等权组合收益：对每天被选中的股票收益取平均（示范）
    df_multi["strategy_ret"] = df_multi["selected_lag1"] * df_multi["ret"]
    portfolio = df_multi.groupby("date")["strategy_ret"].mean()
    print("\nPortfolio return sample:")
    print(portfolio.dropna().head())


if __name__ == "__main__":
    main()

