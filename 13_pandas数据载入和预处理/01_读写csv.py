"""
CSV文件：Comma-Separated Values的缩写，用半角逗号（’,’）作为字段值的分隔符

读取csv:
    pandas.read_csv(filepath_or_buffer, sep=’，’, header=’infer’,
        names=None, index_col=None, dtype=None, engine=None, nrows=None)
    filepath:	接收string，代表文件路径，无默认
    sep: 接收string，代表分隔符。read_csv默认为“,”,read_table默认为制表符“\t”，
         如果分隔符指定错误，在读取数据的时候，每一行数据将连成一片
    header:	接收int或sequence，表示将某行数据作为列名，默认为infer，表示自动识别
    names:	接收array，表示列名，默认为None
    index_col:	接收int、sequence或False，表示索引列的位置，取值为sequence则代表多重索引，默认为None
    dtype:	接收dict，代表写入的数据类型（列名为key，数据格式为values），默认为None
    engine:	接收c或者python，代表数据解析引擎，默认为c
    nrows: 	接收int，表示读取前n行，默认为None
写入csv:
    DataFrame.to_csv(path_or_buf = None, sep = ’,’, na_rep, columns=None,
        header=True, index=True, index_label=None, mode=’w’, encoding=None)

"""
import pandas as pd

print("\n--------1.默认方式读取----------")
df = pd.read_csv("sunspots.csv")
print(df.head(5))

print("\n--------2.指定分隔符----------")
df2 = pd.read_table("sunspots.csv", sep=",")  # 使用read_table，并指定分隔符
print(df2.head(5))

print("\n--------3.将头行也算入df----------")
# 指定列名,将表头行也算入df
df3 = pd.read_csv("sunspots.csv", names=["a", "b"])
print(df3.head(5))
