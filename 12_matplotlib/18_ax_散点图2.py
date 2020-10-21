import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
plt.rcParams['font.family'] = ['SimHei']  # 用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
for color in ['red', 'green', 'blue']:
    n = 500
    x, y = np.random.randn(2, n)  # 返回ndarray,然后拆包成两行 x,y
    ax.scatter(x, y, c=color, label=color, alpha=0.3, edgecolors='none')
    ax.legend()
    ax.grid(True)

plt.show()

ret = np.random.randn(2, 4)
print(type(ret))
print(ret)
