"""
参考:https://blog.csdn.net/weixin_40683253/article/details/87857194

箱线图（boxplot）也称箱须图，其绘制需使用常用的统计量，能提供有关数据位置和分散情况的关键信息,
    尤其在比较不同特征时，更可表现其分散程度差异。

箱线图利用数据中的五个统计量（最小值、下四分位数、中位数、上四分位数和最大值）来描述数据
    它也可以粗略地看出数据是否具有对称性、分布的分散程度等信息，特别可以用于对几个样本的比较。

plt.boxplot(x, notch=None, sym=None, vert=None, whis=None,positions=None,
            widths=None, patch_artist=None,meanline=None, labels=None, … )
    x:          array,表示用于绘制箱线图的数据。无默认。
    positions:  array,表示图形位置。默认为None。
    notch:      boolean,表示中间箱体是否有缺口。默认为None。
    widths:     scalar或者array。表示每个箱体的宽度。默认为None。
    sym:        特定sting。指定异常点形状。默认为None。
    labels:     array。指定每一个箱线图的标签。默认为None。
    vert:       boolean。表示图形是横向纵向; True-纵向，False-横向； 默认为True
    meanline:   boolean。表示是否显示均值线。默认为False。

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2)  # 设置随机种子
# na = np.random.rand(5, 4)
na = np.arange(1, 21).reshape(5, 4)
df = pd.DataFrame(na, columns=['A', 'B', 'C', 'D'])
print(df, end="\n\n")

df.boxplot()  # 或者使用plt.boxplot()

plt.show()
