"""
参考:https://blog.csdn.net/qq_38788128/article/details/80796776
    https://zhuanlan.zhihu.com/p/45832006


哑变量( Dummy Variables)是用以反映质的属性的一个人工变量，是量化了的自变量，通常取值为0或1。
就是不能量化处理的变量进行量化,如工人,农民,学生引入4个哑变量处理:D1(1-工人,0-非工人),D2(1-农民,0-非农民)..

利用pandas库中的get_dummies函数对类别型特征进行哑变量处理。

pandas.get_dummies(data, prefix = None, prefix_sep = '_',
    dummy_na = False, columns = None, sparse = False, drop_first=False)

    data:接收array、DataFrame或者Series。表示需要哑变量处理的数据。无默认。
    prefix:接收string、string的列表或者string的dict。表示哑变量化后列名的前缀。默认为None。
    prefix_sep:接收string。表示前缀的连接符。默认为‘_’。
    dummy_na:接收boolean。表示是否为Nan值添加一列。默认为False。
    columns:接收类似list的数据。表示DataFrame中需要编码的列名。
           默认为None，表示对所有object和category类型进行编码。
    sparse: 接收boolean。表示虚拟列是否是稀疏的。默认为False。
    drop_first: 接收boolean。表示是否通过从k个分类级别中删除第一级来获得k-1个分类级别。默认为False。


"""
import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])

df.columns = ['color', 'size', 'prize', 'class label']
print(df, end="\n\n")
ret_df = pd.get_dummies(df, columns=['color'])  # DataFrame;不指定columns的话，默认对所有非int变量进行哑变量处理
print(ret_df)
