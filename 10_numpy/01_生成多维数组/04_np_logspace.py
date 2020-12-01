"""
生成等比数列
np.logspace(start, stop, num, endpoint=True, base=10.0, dtype=None))
返回numpy.ndarray
    start, stop: 10的幂,默认基数base为10
    num:第三个参数元素个数
    base: 基数
    dtype: 默认float64
"""

import numpy as np

ret = np.logspace(0, 4, 5, base=2)  # 返回numpy.ndarray；2^0~2^4,一共5个数
print(ret)  # [ 1.  2.  4.  8. 16.]
