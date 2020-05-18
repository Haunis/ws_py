
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

