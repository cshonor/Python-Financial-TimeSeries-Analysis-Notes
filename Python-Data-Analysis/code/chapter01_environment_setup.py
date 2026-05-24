"""
第 1 章配套：环境检查 + 显示选项 + 标准导入惯例（对应原书 1.6.1、1.6.3）

运行：
  python Python-Data-Analysis/code/chapter01_environment_setup.py
"""

from __future__ import annotations


def configure_display() -> None:
    """对齐原书常见的 NumPy / pandas 控制台输出风格。"""
    import numpy as np
    import pandas as pd

    np.set_printoptions(precision=4, suppress=True)
    pd.options.display.max_columns = 20
    pd.options.display.max_rows = 20
    pd.options.display.width = 120


def standard_imports_demo() -> None:
    """社区推荐别名（不要用 from numpy import *）。"""
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("numpy :", np.__version__)
    print("pandas:", pd.__version__)

    arr = np.array([1.23456789, 2.34567890])
    print("ndarray sample:", arr)

    df = pd.DataFrame({"a": [1, 2], "b": [3.1, 4.2]})
    print("DataFrame sample:\n", df)
    # plt 仅演示导入成功，不弹窗
    print("matplotlib imported as plt:", plt.__name__)


def optional_stack_check() -> None:
    """检查可选库是否已安装（未安装则提示，不中断）。"""
    optional = ["scipy", "statsmodels", "sklearn", "seaborn"]
    for name in optional:
        try:
            mod = __import__(name)
            ver = getattr(mod, "__version__", "unknown")
            print(f"{name:12s} OK  version={ver}")
        except ImportError:
            print(f"{name:12s} --  not installed (optional)")


def main() -> None:
    print("=== 1) Display options ===")
    configure_display()
    print("\n=== 2) Standard imports ===")
    standard_imports_demo()
    print("\n=== 3) Optional libraries ===")
    optional_stack_check()
    print("\nDone. Next: code/numpy/ then Financial-BigData pandas/")


if __name__ == "__main__":
    main()
