# Matplotlib 显示图表 show

## plt.show()

显示当前创建的所有图形窗口，阻塞程序直到窗口关闭。

## 基本用法

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()  # 弹出窗口显示图表
```

## 说明

- **阻塞**：`show()` 会阻塞后续代码执行，关闭窗口后程序才继续
- **交互模式**：在 `plt.ion()` 下可非阻塞显示
- **保存优先**：若在 `show()` 前执行 `plt.savefig()`，会先保存再显示

## 保存图片

在 `show()` 之前保存，避免空白图：

```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig('output.png', dpi=150)
plt.show()
```

## 关闭图形

```python
plt.close()       # 关闭当前图形
plt.close('all')  # 关闭所有图形
```
