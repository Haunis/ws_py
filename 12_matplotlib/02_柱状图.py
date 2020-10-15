"""
在Pandas中绘制柱状图只需在plot函数中加参数kind = ‘bar’
如果类别较多，可以绘制水平柱状图（kind = ‘barh’）。

"""
import pandas as pd
import matplotlib.pyplot as plt

stu = {'name': ['小明', '王芳', '赵平', '李红', '李涵'],
       'sex': ['male', 'female', 'female', 'female', 'male'],
       'year': [1996, 1997, 1994, 1999, 1996]}
data = pd.DataFrame(stu)

ret_se = data['sex'].value_counts()  # Series
# ret_se = data['sex'].groupby(data['sex']).count()  # 和上面的ret_se结果一样
# ret_se = data['sex'].groupby(data['sex']).size()  # 和上面的ret_se结果一样

print(ret_se)
ret_se.plot(kind='bar', rot=3)
plt.show()
