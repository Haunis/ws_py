"""
fig.savefig(save_path, format='png', transparent=True, dpi=300, pad_inches = 0)
    fname:包含文件路径或Python文件型对象的字符串。图片格式是从文件扩展名中推断出来的（例如pdf格式的.pdf）
    dpi :设置每英寸点数的分辨率，默认为100
    facecolor，edgecolor	子图之外的图形背景颜色，默认是’w’（白色）
    format:	文件格式（’png’,’pdf’,’svg’,’ps’等）
    bbox_inches:要保存的图片范围，如果设置为‘tight‘则去除图片周围的空白

"""
import matplotlib.pyplot as plt
import numpy as np

na = np.arange(0, np.pi * 2, 0.01)
fig = plt.figure(figsize=(8, 4), dpi=90)  # 确定画布大小
axe = fig.add_subplot(1, 1, 1)
plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xlim(0, np.pi * 2)
plt.ylim(-1.2, 1.2)
plt.plot(na, np.sin(na))
plt.show()

fig.savefig("./temp.png")
