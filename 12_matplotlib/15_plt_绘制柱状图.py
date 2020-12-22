"""

"""
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['SimHei']  # 显示中文

data = [25, 30, 32, 34, 34, 23]
label = ['青海', '兰州', '北京', '上海', '广州', '拉萨']
plt.xticks(range(len(data)), labels=label)
plt.xlabel('城市')  # x轴上设置标签
plt.ylabel('温度')  # y轴上设置标签
plt.title('六城市8月份日均最高气温')
plt.bar(range(len(data)), data)
for x, y in zip(range(len(data)), data):
    print("x =%d,y=%d" % (x, y))
    plt.text(x, y, y, ha='center', va='top')
    # plt.text(x, y, 100, ha='center', va='top')
plt.show()
