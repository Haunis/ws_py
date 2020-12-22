import pandas as pd
import numpy as np

se = pd.Series(np.arange(1, 11))
print(se)
print("\nse.mean():", se.mean())
print("se.std():", se.std())


