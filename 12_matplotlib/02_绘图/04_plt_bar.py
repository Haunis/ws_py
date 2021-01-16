"""

"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 6)

# y1 = np.random.uniform(1.5, 1.0, 5) #从一个均匀分布中随机采样[1.5,1.0),采取5个
# y2 = np.random.uniform(1.5, 1.0, 5)
y1 = 2 * x
y2 = 4 * x
plt.bar(x, y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
plt.bar(x + 0.35, y2, width=0.35, facecolor='yellowgreen', edgecolor='white')
plt.show()
