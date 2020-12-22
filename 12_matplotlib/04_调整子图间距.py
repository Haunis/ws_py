"""
plt.subplots_adjust()
    调整子图之间的距离，在pycharm不生效。
"""
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 3, sharex=True, sharey=True)
for i in range(3):
    for j in range(3):
        axes[i, j].hist(np.random.randn(500), bins=50, color='r', alpha=0.1)  # 直方图
plt.subplots_adjust(wspace=0, hspace=0)  # 在pycharm设置无效,jupyter notebook是ok的
plt.show()
