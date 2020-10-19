import pandas as pd
import numpy as np

se = pd.Series(np.arange(1, 11))
print(se)
print("se.mean():", se.mean())
print("se.std():", se.std())
ret_se = se.mean() - 3 * se.std() > se  # ret是存储bool的series
print(ret_se)
ret = np.arange(se.shape[0])[ret_se]
print(type(ret))
print(ret)
