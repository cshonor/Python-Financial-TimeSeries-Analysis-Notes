"""
第 12 章配套：Patsy 设计矩阵 + statsmodels OLS / AutoReg

依赖（按需安装）：
  pip install patsy statsmodels pandas numpy

运行：
  python Python-Data-Analysis/code/chapter12_statsmodels_demo.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def demo_patsy(df: pd.DataFrame) -> None:
    import patsy

    print("=== 12.2 Patsy dmatrices ===")
    y, X = patsy.dmatrices("ret ~ pe + C(industry)", data=df, return_type="dataframe")
    print("y columns:", list(y.columns))
    print("X columns:", list(X.columns))
    print(X.head(3))

    print("\n=== 12.2.1 build_design_matrices (OOS) ===")
    train, test = df.iloc[:6], df.iloc[6:]
    y_tr, X_tr = patsy.dmatrices("ret ~ pe + C(industry)", data=train, return_type="dataframe")
    y_te, X_te = patsy.build_design_matrices(
        [y_tr.design_info, X_tr.design_info], test, return_type="dataframe"
    )
    print("test y/X shapes:", y_te.shape, X_te.shape)


def demo_ols(df: pd.DataFrame) -> None:
    import statsmodels.formula.api as smf

    print("\n=== 12.3 OLS formula API ===")
    res = smf.ols("ret ~ pe + C(industry)", data=df).fit()
    print(res.summary().as_text().split("\n")[:12])
    print("params:\n", res.params)


def demo_autoreg() -> None:
    from statsmodels.tsa.ar_model import AutoReg

    print("\n=== 12.3.2 AutoReg ===")
    rng = np.random.default_rng(0)
    idx = pd.date_range("2020-01-01", periods=120, freq="B")
    ar = pd.Series(rng.normal(0, 0.01, len(idx)), index=idx)
    for t in range(1, len(ar)):
        ar.iloc[t] += 0.3 * ar.iloc[t - 1]
    fit = AutoReg(ar, lags=5, old_names=False).fit()
    print(fit.params.head())


def main() -> None:
    rng = np.random.default_rng(1)
    n = 12
    df = pd.DataFrame(
        {
            "ret": rng.normal(0.001, 0.02, n),
            "pe": rng.uniform(5, 30, n),
            "industry": rng.choice(["bank", "tech"], n),
        }
    )

    try:
        import patsy  # noqa: F401
    except ImportError:
        print("patsy not installed: pip install patsy")
        return

    demo_patsy(df)

    try:
        import statsmodels  # noqa: F401
    except ImportError:
        print("\nstatsmodels not installed: pip install statsmodels")
        return

    demo_ols(df)
    demo_autoreg()
    print("\nDone. See: Python-Data-Analysis/code/statsmodels/")


if __name__ == "__main__":
    main()
