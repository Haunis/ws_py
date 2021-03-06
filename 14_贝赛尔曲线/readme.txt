贝塞尔曲线的的定义:
    https://baike.baidu.com/item/%E8%B4%9D%E5%A1%9E%E5%B0%94%E6%9B%B2%E7%BA%BF/1091769?fr=aladdin
    https://www.zhihu.com/question/29565629

三阶贝塞尔曲线预览图:
    https://cubic-bezier.com/


一阶贝塞尔曲线(2个控制点):
B(t) = p0 + (p1-p0)*t = p0*(1-t)+p1*t

二阶贝塞尔曲线(三个控制点):
B(t) = p0*(1-t)^2 + 2*p1*(1-t)*t + p2*t^2

三阶贝塞尔曲线(4个控制点):
B(t) = p0*(1-t)^3 + 3*p1*(1-t)^2 *t + 3*p2*(1-t)*t^2 +p3*t^3;


所谓贝塞尔曲线就是在t[0,1]时间内，每个特定时刻的t都会有x = x(t)和y = y(t)值
在一个二维坐标系内，将所有(x,y)这些点绘制出来就是贝塞尔曲线

如何绘制曲线：
    绘制曲线最直接的方法就是找出y = f(x)的函数关系，绘制出来就行
    一阶,二阶还好找出y关于x的映射关系，但三阶甚至高阶就不好找到y = f(x)的函数关系了

    这个时候可以考虑使用近似值求解法：
        即在x = x0时，求解出此时t的值t0，再代入y = y(t)求解出此时y0即可

        如何求出x = x0时t的值？
        循环设t的值，比如遍历range(0,1,0.01)，在某个t0'时刻 x0' = x(t0'),
        如果x0'-x0差距小于某个可接受的值(如0.0001)就认为t0'是x = x0的解

