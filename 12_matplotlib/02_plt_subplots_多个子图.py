"""
就是创建子图序列: fig,axes=plt.subplots(2,3)
"""
import matplotlib.pyplot as plt

# 创建1个figure,里面有2*3个子图
fig, axes = plt.subplots(2, 3)  # axes是二维ndarray;
print(axes.shape)  # (2,3)即2行3列的数组

fig.add_subplot(2, 3, 1)  # 在第一个子图上画
plt.plot([4, 3, 2, 1])

axes[0, 1].plot([1, 2, 3, 4])  # 在第二个子图话
axes[1][2].plot([1, 2, 3, 4])  # 在最后一个子图画

plt.show()
