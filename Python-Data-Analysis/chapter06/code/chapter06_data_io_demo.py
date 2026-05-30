"""
第 6 章配套：数据加载、存储与文件格式（CSV / JSON / 分块写出）

运行：
  python Python-Data-Analysis/code/chapter06_data_io_demo.py

Excel: pip install openpyxl 后取消脚本内 excel 演示注释
SQL:   pip install sqlalchemy 并配置连接后使用 read_sql
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path


def demo_read_write_csv() -> None:
    import pandas as pd

    print("\n=== 6.1 read_csv / to_csv ===")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "ohlcv.csv"
        path.write_text(
            "date,open,close,volume\n"
            "2025-01-01,10.0,10.1,1000\n"
            "2025-01-02,10.1,NA,1100\n"
            "2025-01-03,10.2,10.4,900\n",
            encoding="utf-8",
        )

        df = pd.read_csv(
            path,
            parse_dates=["date"],
            index_col="date",
            na_values=["NA", ""],
        )
        print("read_csv:\n", df)

        out = Path(tmp) / "out.csv"
        df.to_csv(out, na_rep="NULL")
        print("to_csv content:\n", out.read_text(encoding="utf-8"))


def demo_chunksize() -> None:
    import pandas as pd

    print("\n=== 6.1.1 chunksize ===")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "big.csv"
        lines = ["date,ret\n"] + [f"2025-01-{i:02d},{0.01 * i}\n" for i in range(1, 8)]
        path.write_text("".join(lines), encoding="utf-8")

        total = 0.0
        n = 0
        for chunk in pd.read_csv(path, chunksize=3):
            total += chunk["ret"].sum()
            n += len(chunk)
        print("chunks processed rows:", n, "sum ret:", total)


def demo_json() -> None:
    import pandas as pd

    print("\n=== 6.1.4 JSON ===")
    payload = [
        {"code": "000001", "close": 10.1},
        {"code": "000002", "close": 20.3},
    ]
    s = json.dumps(payload)
    df = pd.read_json(s)
    print(df)
    print("to_json:", df.to_json(orient="records"))


def demo_whitespace_sep() -> None:
    import pandas as pd

    print("\n=== 6.1 sep=regex (whitespace) ===")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "space.txt"
        path.write_text("a    b    c\n1    2    3\n", encoding="utf-8")
        df = pd.read_csv(path, sep=r"\s+")
        print(df)


def main() -> None:
    try:
        import pandas as pd  # noqa: F401
    except ImportError:
        print("请先安装: pip install pandas")
        return

    demo_read_write_csv()
    demo_chunksize()
    demo_json()
    demo_whitespace_sep()

    print("\n--- 未在本脚本自动运行（需额外依赖）---")
    print("Excel: pd.read_excel / df.to_excel  (openpyxl)")
    print("HDF5:  pd.HDFStore  (tables/pytables)")
    print("API:   requests.get(url); pd.DataFrame(resp.json())")
    print("SQL:   pd.read_sql(sql, sqlalchemy.create_engine(...))")
    print("\nDone.")


if __name__ == "__main__":
    main()
