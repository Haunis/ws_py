import pandas as pd
import matplotlib.pyplot as plt

stu = {'name': ['小明', '王芳', '赵平', '李红', '李涵'],
       'sex': ['male', 'female', 'female', 'female', 'male'],
       'year': [1996, 1997, 1994, 1999, 1996]}
data = pd.DataFrame(stu)

ret_se = data['sex'].value_counts()  # Series
print(data['sex'].)
print(ret_se)
ret_se.plot(kind='bar', rot=3)
plt.show()
