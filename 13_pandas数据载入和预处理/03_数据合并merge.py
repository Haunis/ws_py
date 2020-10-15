"""
merge函数是通过一个或多个键将两个DataFrame按行合并起来，与SQL中的 join 用法类似.
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
    left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'),
    copy=True, indicator=False, validate=None)

    left:	参与合并的左侧DataFrame
    right:	参与合并的右侧DataFrame
    how:	连接方法:inner，left，right，outer
    on:	用于连接的列名
    left_on:	左侧DataFrame中用于连接键的列
    right_on:	右侧DataFrame中用于连接键的列
    left_index:	左侧DataFrame中行索引作为连接键
    right_index:	右侧DataFrame中行索引作为连接键
    sort:	合并后会对数据排序，默认为True
    suffixes:	修改重复名
"""
import pandas as pd

df_price = pd.DataFrame({'fruit': ['apple', 'grape', 'orange', 'orange'],
                         'price': [8, 7, 9, 11]})
df_amount = pd.DataFrame({'fruit': ['apple', 'grape', 'orange'],
                          'amout': [5, 11, 8]})
# display(df_price, amount, pd.merge(df_price, amount))
ret_def = pd.merge(df_price, df_amount, how="outer")  # 默认inner_join
print("df_price:")
print(df_price)

print('df_amount:')
print(df_amount)

print("ret_def:")
print(ret_def)
