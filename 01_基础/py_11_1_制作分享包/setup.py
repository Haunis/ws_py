"""
制作分享包
    1.先建立一个要分享的包,如my_package
    2.创建 setup.py,在里面设置固定参数
    3.构建模块:
        控制台运行: python3 setup.py build
    4.生成发布压缩包
        控制台运行: python3 setup.py sdist
"""
from distutils.core import setup

setup(
    name="my_pakege",  # 包名
    version="1.0",
    description="测试发布包",  # 描述信息
    long_description="测试发布包详细信息",  # 详细描述信息
    author="xiao_ming",  # 作者
    author_email="xiao_ming@126.com",  # 作者邮箱
    url="www.xiaoming.com",  # 个人主页
    py_modules=["my_package.cat", "my_package.dog"]  # 包里模块
)
