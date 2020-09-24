"""
生成等差数列
np.linspace(start, stop, num, endpoint, retstep=False, dtype=None)
返回numpy.ndarray
    start:	起始值，默认从0开始;
    stop: 	结束值；生成的元素<<<包括结束值>>>
    num:	要生成的等间隔样例数量

"""
import numpy as np

ret = np.linspace(0, 9, 10)  # 从0到9生成10个,包含start也包含stop
print(ret)
print("type(ret):", type(ret))  # numpy.ndarray
