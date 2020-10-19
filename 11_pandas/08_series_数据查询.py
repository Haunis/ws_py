import numpy as np
import pandas as pd

se = pd.Series(np.arange(0, 4))
print(se)

print("\n-------------se[ndarray]---------------")
ret = se[np.array([0, 1])]
print(ret)

print("\n-------------iloc---------------")
ret_se = se.iloc[np.array([0, 1])]  # 取第0，第1两个元素
print(ret_se)
