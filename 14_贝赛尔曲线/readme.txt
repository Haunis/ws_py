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