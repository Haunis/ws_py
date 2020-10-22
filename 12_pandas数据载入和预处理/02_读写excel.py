"""
读取excel:
pandas.read_excel(io, sheetname, header=0, index_col=None, names=None, dtype)
    pd.read_excel()会将读取到的第一行作为字段
    io:	string,文件路径
    sheetname:	接收string、int，代表excel表内数据的分表位置，默认为0
    header:	接收int或sequence，表示将某行数据作为列名，默认为infer，表示自动识别
    names:	接收int、sequence或者False，表示索引列的位置，取值为sequence则代表多重索引，默认为None
    index_col:	接收int、sequence或者False，表示索引列的位置，取值为sequence则代表多重索引，默认为None
    dtype:	接收dict，代表写入的数据类型（列名为key，数据格式为values），默认为None

写入excel:
DataFrame.to_excel(excel_writer=None, sheetname=None’, na_rep=”, header=True,
    index=True, index_label=None, mode=’w’, encoding=None)
    与 to_csv方法的常用参数基本一致，区别之处在于指定存储文件的文件路径参数excel_writer,
    增加了一个sheetnames参数，用来指定存储的Excel sheet的名称，默认为sheet1

"""
import pandas as pd

print("\n-------------1.读取excel----------------")
xlsx = "./data_test.xlsx"
df1 = pd.read_excel(xlsx, "Sheet1")
print(df1)

print("\n-------------2.指定Sheet----------------")
df2 = pd.read_excel("./data_test.xlsx", "Sheet1")
print(df2)
