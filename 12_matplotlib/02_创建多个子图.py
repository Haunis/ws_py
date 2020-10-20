"""
就是创建子图序列: fig,axes=plt.subplots(2,3)
"""
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3)  # axes是二维ndarray;创建2*3个子图
print(axes.shape)  # (2,3)即2行3列的数组
# axes[1,2].plot([1,2,3,4])
axes[1][2].plot([1, 2, 3, 4])  # 两个一样
plt.show()
