"""
判断各行和前面的相比,是否是重复数据:
    drop_duplicates(self, subset=None, keep=’first’, inplace=False)
    返回一个bool的series

    subset:接收string或sequence，表示进行去重的列，默认全部列
    keep:first--默认值,保留第一个出现的,其后出现的重复值都删除
        last--与first相反,保留最后一个出现的
    inplace:接收布尔型数据，表示是否在原表上进行操作，默认为False

"""
import pandas as pd

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 1, 4, 4],
                     'k3': [1, 1, 5, 2, 1, 4, 4]})
print(data, end="\n\n")

print("\n-------------1.获取重复行------------------")
ret = data.duplicated()
print(ret, end="\n\n")

print("\n-------------2.删除重复行------------------")
ret_df = data.drop_duplicates()  # 删除重复行
print(ret_df)

print("\n-------------3.指定列重复时,删除重复行------------------")
ret_def = data.drop_duplicates(['k2', 'k3'])
print(ret_def)

print("\n-------------4.指定列重复时,删除重复行,keep=last------------------")
# 去重时,保留最后出现的记录;保留第一个出现的
ret_def = data.drop_duplicates(['k2', 'k3'], keep='last')
print(ret_def)
