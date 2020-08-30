
1.安装pip3
    sudo apt-get install python3-pip
2.安装pygame
    sudo pip3 install pygame (会报错,这个时候可以使用 sudo -H pip3 install pygame )
    或者 pip3 install pygame ,安装在当前用户目录下

3.卸载pygame
    sudo pip3 uninstall pygame


pip install
    调用python中的pip库,可使用pip show pip查看调用哪个库
安装位置:
    一般为($(python安装目录)\lib\site-packages
更改pip安装库的位置: 修改python安装目录下的site.py



pip原理：
    python第三方库的管理网站（俗称源）是：https://pypi.python.org/pypi
    当用户使用命令pip install pip,就是会向上面的网站发送包搜索请求,如果找不到的话，重试几次以后放弃。
    如果找到的话，就会下载那个相关库对应的代码和依赖，下载完成后在本地编译。
    本地编译完成以后，安装到本地的python的安装目录(一般为($(python安装目录)\lib\site-packages))。


pip常见命令：
   pip3 list         查看已安装的包
   pip3 show xxx     查看已安装包的信息，如pip3 show pip