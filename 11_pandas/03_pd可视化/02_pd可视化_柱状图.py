"""
在Pandas中绘制柱状图只需在plot函数中加参数kind = ‘bar’
如果类别较多，可以绘制水平柱状图（kind = ‘barh’）。

"""
import pandas as pd
import matplotlib.pyplot as plt

dict_temp = {
    'name': ['小明', '王芳', '赵平', '李红', '李涵'],
    'sex': ['male', 'female', 'female', 'female', 'male'],
    'year': [1996, 1997, 1994, 1999, 1996]
}
df = pd.DataFrame(dict_temp)
print(df)

ret_se = df['sex'].value_counts()  # Series
# ret_se = df['sex'].groupby(df['sex']).count()  # 和上面的ret_se结果一样
# ret_se = df['sex'].groupby(df['sex']).size()  # 和上面的ret_se结果一样
"""
female    3
male      2
"""

print("\nret_se:\n%s" % ret_se.__str__())
ret_se.plot(kind='bar', rot=3)
plt.show()
