import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

na = np.random.rand(6, 4)
na = np.arange(1, 25).reshape(6, 4)
df = pd.DataFrame(na,
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
print(df)
df.plot.bar()  # index为x轴上分组,每组是na每行的统计
plt.show()
