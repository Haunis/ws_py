import sys
import pandas as pd

print("version:%s" % sys.version)
print("location: %s" % sys.executable)
print("数据挖掘")

print("pd.__file__:%s"%pd.__file__)
data=pd.read_csv('train.csv')
print(data.head())
print(data.isnull().sum())