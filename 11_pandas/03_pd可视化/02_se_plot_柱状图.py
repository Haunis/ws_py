"""
在Pandas中绘制柱状图只需在plot函数中加参数kind = ‘bar’
如果类别较多，可以绘制水平柱状图（kind = ‘barh’）。

直方图（Histogram）又称质量分布图，是统计报告图的一种
由一系列高度不等的纵向条纹或线段表示数据分布的情况，一般用横轴表示数据所属类别，纵轴表示数量或者占比。

用直方图可以比较直观地看出产品质量特性的分布状态，便于判断其总体质量分布情况
直方图可以发现分布表无法发现的数据模式、样本的频率分布和总体的分布

"""
import pandas as pd
import matplotlib.pyplot as plt

dict_temp = {
    'name': ['小明', '王芳', '赵平', '李红', '李涵'],
    'sex': ['male', 'female', 'female', 'female', 'male'],
    'year': [1996, 1997, 1994, 1999, 1996]
}
df = pd.DataFrame(dict_temp)
print(df)

ret_se = df['sex'].value_counts()  # Series
# ret_se = df['sex'].groupby(df['sex']).count()  # 和上面的ret_se结果一样
# ret_se = df['sex'].groupby(df['sex']).size()  # 和上面的ret_se结果一样
"""
female    3
male      2
"""

print("\nret_se:\n%s" % ret_se.__str__())

fig, axes = plt.subplots(1, 3)
ret_se.plot(ax=axes[0], color='r', kind='bar', rot=3)  # ret_se索引对应横坐标，value对应纵坐标
ret_se.plot.bar(ax=axes[1], color='g', alpha=0.7)  # 垂直柱状图
ret_se.plot.barh(ax=axes[2], color='b', alpha=0.7)
plt.show()
