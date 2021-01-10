"""
绘制柱状图:
    plt.bar(x,y)
    或者pd.Series(data=data, index=label).plot(kind='bar')

绘制文字:
     plt.text(x, y, y, ha='center', va='top', color='r', fontsize=22)
        在x,y处绘制y
        ha: left,center,right   水平方向文字的位置
        va: top,bottom          竖直方向文字的位置

"""
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = ['SimHei']  # 显示中文

data = [11, 12, 13, 14, 15, 16]
label = ['青海', '兰州', '北京', '上海', '广州', '拉萨']
plt.xticks(ticks=range(len(data)), labels=label)  # 设置x轴刻度，可以设置标签
plt.xlabel('城市')  # x轴上设置标签
plt.ylabel('温度')  # y轴上设置标签
plt.title('六城市8月份日均最高气温')

# pd.Series(data=data, index=label).plot(kind='bar') #ok
plt.bar(range(len(data)), data)  # 绘制柱状图

for x, y in zip(range(len(data)), data):
    print("x =%d,y=%d" % (x, y))
    plt.text(x, y, y, ha='center', va='bottom', color='r', fontsize=22)  # 在某个位置绘制文字
plt.show()
