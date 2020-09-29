"""

"""

import pandas as pd

index1 = range(10, 14)
index2 = "hello the cruel world".split()
val = [2, 4, 5, 6]

s0 = pd.Series(val)
s1 = pd.Series(val, index=index1)
s2 = pd.Series(val, index=index2)
print("s0.index:", s0.index)  # s0.index是RangeIndex对象
print("s1.index:", s1.index)
print("s2.index:", s2.index)

print("s0[0]:", s0[0])
print("s1[10]:", s1[10])  # ,s1[0]   #wrong
print('s2[0]:', s2[0], ",s2['hello']:", s2["hello"])
