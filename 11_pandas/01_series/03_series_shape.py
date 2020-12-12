"""
Series.shape: 返回一个元组
"""
import pandas as pd

se = pd.Series([10, 20, 30, 40])
print("se:\n%s" % se.__str__())
ret_tuple = se.shape
print("ret_tuple:", ret_tuple)  # (4,)
