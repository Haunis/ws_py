"""
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None,
    autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1,
    startangle=None, radius=None, … )

    x       :array。表示用于绘制撇的数据。无默认。
    autopct	:string。指定数值的显示方式。默认为None
    explode	:array。表示指定项离饼图圆心为n个半径。默认为None
    pctdistance: float。指定每一项的比例和距离饼图圆心n个半径。默认为0.6
    labels:     array。指定每一项的名称。默认为None
    labeldistance: float。指定每一项的名称和距离饼图圆心多少个半径。默认为1.1
    color:      string或者包含颜色字符串的array。表示饼图颜色。默认为None
    radius:     float。表示饼图的半径。默认为1。
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))  # 画布大小
plt.rcParams['font.family'] = ['SimHei']  # 中文显示

labels = '春', '夏', '秋', '冬'  # 每块小饼的名称
x = [15, 30, 45, 10]  # 建立轴的大小
explode = (0.05, 0.05, 0.05, 0.5)  # 饼和饼之间的距离;这个是控制分离的距离的，默认饼图不分离

# qutopct在图中显示比例值，注意值的格式; 1.1f小数点前的1代表输出总宽度
plt.pie(x, labels=labels, explode=explode, startangle=60, autopct='%1.1f%%')

plt.title('Rany days by season')
plt.tick_params(labelsize=20)
plt.show()
