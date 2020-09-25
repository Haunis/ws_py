"""
np.loadtxt(fname, dtype=, comments=’#’, delimiter=None, converters=None,
        skiprows=0, usecols=None, unpack=False, ndmin=0, encoding=‘bytes’)
    fname：	str，读取的CSV文件名
    delimiter：str，数据的分割符
    usecols： tuple ，执行加载数据文件中的哪些列
    unpack： bool，是否将加载的数据拆分为多个组，True表示拆，False不拆
    skipprows： int，跳过多少行，一般用于跳过前几行的描述性文字
    encoding： bytes，编码格式

"""