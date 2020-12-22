"""
已定义好的函数可以通过以下三种方法应用到数据：
    1. map函数：将函数套用到Series的每个元素中;
        Series.map(function):就是对Series的每个元素进行操作
    2. apply函数，将函数套用到DataFrame的行或列上，行与列通过axis参数设置
        就是对每一行/列使用某个函数
    3. applymap函数，将函数套用到DataFrame的每个元素上。

"""
import pandas as pd
import numpy as np


def fun_split(x):  # series.map(f) 就是对series的每个元素进行操作
    return x.split('元')[0]  # 这里的操作是 将str切割并只取第一个元素,就是去掉'元'


def main():
    print("\n-------------1.series.map(f)----------------")
    data = {
        'fruit': ['apple', 'grape', 'banana'],
        'price': ['30元', '43元', '28元']
    }
    df = pd.DataFrame(data)
    print(df)
    df['price'] = df['price'].map(fun_split)  # df['price']返回的是Series;
    print('修改后的数据表:\n', df)

    print("\n-------------2.df.apply(np.fun)----------------")
    li = [x for x in range(9)]
    ret_ndarray = np.array(li).reshape(3, 3)
    df = pd.DataFrame(ret_ndarray, columns=['c1', 'c2', 'c3'], index=['app', 'win', 'mac'])
    print("df:\n%s" % df.__str__())
    df2 = df.apply(np.mean)  # np.mean是个函数; 默认是每一列的平均值
    print("\ndf.apply(np.mean):\n%s" % df2.__str__())

    print("\n-------------3.df.applymap()----------------")
    print("before:\n", df)
    # df2 = df.applymap(lambda x: '%.3f' % x)   # 保留小数点后三位
    df2 = df.applymap(lambda x: x * 2)  # 每个数乘以2
    print("\nafter:\n", df2)


if __name__ == "__main__":
    main()
