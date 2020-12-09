"""
对于DataFrame数据排序，通过指定轴方向，使用sort_index函数对行或列索引进行排序。
如果要进行列排序，则通过sort_values函数把列名传给by参数即可。

和Series排序对照来看
"""
import pandas as pd

data = {'fruit': ['apple', 'grape', 'banana'], 'price': [70, 40, 50]}
df = pd.DataFrame(data)
print(df)

df2 = df.sort_values(by='price', ascending=False)  # 对price列进行排序;降序
print(df2)
