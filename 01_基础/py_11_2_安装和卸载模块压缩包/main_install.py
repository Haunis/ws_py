"""
解压和安装:
    拿到一个如 my_pakege-1.0.tar.gz 的压缩包后,压缩和安装后即可使用
    1. 解压压缩包:  tar -xvf my_pakege-1.0.tar.gz
    2. 安装压缩包: 进入解压好的目录后执行 sudo python3 setup.py install
    安装路径:/usr/local/lib/python3.6/dist-packages/my_pakege-1.0.egg-info

卸载:
    到包的安装目录下删除安装的包即可
    1.查看包的路径 print(my_package.__file__) #如/usr/local/lib/python3.6/dist-packages/my_package/
    2.到目录夏,rm -rf my_package*

"""

# 报错,pycharm貌似不能识别/usr/local/lib/python3.6/dist-packages/my_package/; 可以在控制台执行
# 解决:解释器切换到系统解释器即可
import my_package

print(my_package.__file__)
