"""

"""
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(0, np.pi * 2, 0.01)
fig1 = plt.figure(figsize=(8, 4), dpi=90)  # 确定画布大小
ax1 = fig1.add_subplot(1, 2, 1)  # 绘制第1幅子图
plt.title('lines example')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.plot(data, data ** 2)
plt.plot(data, data ** 3)
plt.legend(['y = x^2', 'y = x^3'])

ax2 = fig1.add_subplot(1, 2, 2)  # 绘制第2幅子图
plt.title('sin/cos')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, np.pi * 2)
plt.ylim(-1, 1)
plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.plot(data, np.sin(data))
plt.plot(data, np.cos(data))
plt.legend(['sin', 'cos'])
plt.show()
