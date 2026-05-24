# Matplotlib 第一个绘图程序

## 步骤

1. 导入 `pyplot` 模块，使用 `plt` 别名
2. 用 NumPy 的 `arange()` 创建 x 轴数据
3. 计算 y 轴数据
4. 使用 `plt.plot()` 绘图
5. 使用 `plt.show()` 显示图表

## 示例代码

```python
from matplotlib import pyplot as plt
import numpy as np

# 创建 -50 到 50 的 ndarray 作为 x 轴数据
x = np.arange(-50, 50)

# 简单示例：y = x^2
y = x ** 2
plt.plot(x, y)
plt.title("y = x^2")
plt.show()
```

## 说明

- `plt.plot(x, y)`：绘制折线图，第一个参数为 x，第二个为 y
- `plt.title()`：设置图表标题
- `plt.show()`：显示图形窗口，阻塞直到窗口关闭
