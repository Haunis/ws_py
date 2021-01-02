"""
连续变量的离散化
    1. 等宽法
        pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3)
            x	接收array或Series，待离散化的数据
            bins	接收int、list、array和tuple。若为int指离散化后的类别数目，
                    若为序列型则表示进行切分的区间，每两个数的的间隔为一个区间
            right	接收boolean，代表右侧是否为闭区间，默认为True
            labels	接收list、array，表示离散化后各个类别的名称，默认为空
            retbins	接收boolean，代表是否返回区间标签，默认为False
            precision	接收int，显示标签的精度，默认为3
    2. 等频法
         cut函数虽然不能够直接实现等频离散化，但可以通过定义将相同数量的记录放进每个区间。
    3. 聚类分析法(本Demo不涉及)
      一维聚类的方法包括两步，首先将连续型数据用聚类算法进行聚类，
      然后处理聚类得到的簇，为合并到一个簇的连续型数据做同一标记。

分位数:就是用概率作为依据将一批数据分开的那个点
    https://www.zhihu.com/question/67763556
"""
import numpy as np
import pandas as pd

# np.random.seed(666)
na = np.random.randint(25, 100, size=10)  # 返回ndarray
print('原始数据：\n', na, end="\n\n")

print("--------------1.pd.cut()---------------")
bins = [0, 59, 70, 80, 100]
score_cut = pd.cut(na, bins)  # 返回Categorical
ret_se = pd.value_counts(score_cut)  # 统计每个区间人数
print(ret_se)

print("\n------------2.等频法离散化连续型数据---------------")


def SameRateCut(data, k):
    k = 3
    w = data.quantile(np.arange(0, 1 + 1.0 / k, 1.0 / k)) #series
    print("原始数据：\n%s"%w.__str__())
    data = pd.cut(data, w)
    return data


result = SameRateCut(pd.Series(na), 3)
ret = result.value_counts()
print("\n切割后：\n%s"%ret.__str__())
