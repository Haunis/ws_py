"""
二阶贝塞尔公式:
B(t) = p0*(1-t)^2 + 2*p1*(1-t)*t + p2*t^2
"""
from ControlPoint import Point
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p0 = Point(0, 0)  # 开始的控制点
p1 = Point(2, 0.4)  # 中间的控制点,该控制点决定最终曲线的形状
p2 = Point(1, 0)  # 结束的控制点


# 获取t时刻x的值
def get_bezier_x(t):
    # B(t) = p0*(1-t)^2 + 2*p1*(1-t)*t + p2*t^2
    u = 1 - t
    uu = u * u
    tt = t * t

    value = p0.x * uu
    value += 2 * p1.x * u * t
    value += p2.x * tt

    return value


# 获取t时刻y的值
def get_bezier_y(t):
    # B(t) = p0*(1-t)^2 + 2*p1*(1-t)*t + p2*t^2
    u = 1 - t
    uu = u * u
    tt = t * t

    value = p0.y * uu
    value += 2 * p1.y * u * t
    value += p2.y * tt
    return value


tolerance = 0.001


# 采用逼近法求取特定x坐标对应的t
def get_t_from_x(x):
    t = 0;
    diff = x - get_bezier_x(t)
    while abs(diff) > tolerance:
        t = t + 1 / 4096
        diff = x - get_bezier_x(t)
    return t


if __name__ == "__main__":
    se = pd.Series(np.arange(0, 1, 0.08))  # 时间t序列
    se_x = se.map(get_bezier_x)  # t对应的x序列
    se_y = se.map(get_bezier_y)  # t对应的y序列

    # fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(14, 8))
    # axes[0, 0].plot(se, se_x)
    # axes[0, 1].plot(se, se_y)
    # axes[1, 0].plot(se_x, se_y)

    plt.rcParams['font.family'] = ['SimHei']  # 中文显示
    plt.subplot(2, 2, 1)
    plt.plot(se, se_x)  # x关于t的曲线
    plt.title('x = x(t)')
    plt.xlim(0, 1)  # 范围
    plt.ylim(0, 1)  # 范围

    plt.subplot(2, 2, 2)
    plt.plot(se, se_y)  # y关于t的曲线
    plt.title('y = y(t)')
    plt.xlim(0, 1)  # 范围
    plt.ylim(0, 1)  # 范围

    plt.subplot(2, 2, 3)
    plt.plot(se_x, se_y, marker='o')  # y关于x的曲线
    plt.title('y = f(x)')
    # plt.xlim(0, 1)  # 范围
    plt.ylim(0, 1)  # 范围

    plt.subplot(2, 2, 4)
    se_t = se.map(get_t_from_x)  # 这里将se看做x序列,返回对应t序列
    se_t_y = se_t.map(get_bezier_y)  # 拿到x对应的t后,获取此时的y
    plt.plot(se, se_t_y)  # y关于x的曲线
    plt.title('y = f(x),第二种求解方式')
    # plt.xlim(0, 1)  # 范围
    plt.ylim(0, 1)  # 范围

    plt.show()
