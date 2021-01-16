"""
plt.pie(x, explode=None, labels=None, colors=None,
    autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1,
    startangle=None, radius=None, … )

    x:          array。表示用于绘制的数据。
    labels:     array。指定每一项的名称。默认为None
    autopct:    string。指定数值的显示方式,如'%1.3f%%'表示小数点保持3位； 默认为None
    explode:    array。每块三角饼饼尖离圆心距离，如0.5表示离圆心0.5倍半径；默认为None
    pctdistance: float。指定每一项的比例和距离饼图圆心n个半径。默认为0.6
    labeldistance: float。指定每一项的名称和距离饼图圆心多少个半径。默认为1.1
    color:      string或者包含颜色字符串的array。表示饼图颜色。默认为None
    radius:     float。表示饼图的半径。默认为1。
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))  # 画布大小
plt.rcParams['font.family'] = ['SimHei']  # 中文显示
plt.title('饼状图')
plt.tick_params(labelsize=20)

x = [15, 30, 45, 10]  # 每块饼的大小
# labels = '春', '夏', '秋', '冬'  # ok； 元组也行
labels = ['春', '夏', '秋', '冬']  # 每块饼的名称
explode = (0.05, 0.05, 0.05, 1)  # 饼和饼之间的距离;这个是控制分离的距离的，默认饼图不分离

# autopct在图中显示比例值，注意值的格式; 1.1f小数点前的1代表输出总宽度
plt.pie(x, labels=labels, explode=explode, startangle=60, autopct='%1.3f%%')

plt.show()
