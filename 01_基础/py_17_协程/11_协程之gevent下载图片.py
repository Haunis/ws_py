# -*-coding:utf-8-*-
"""
使用gevent的demo

网络请求某个url:
    req = urllib.request.urlopen(url)
    data = req.read()

"""
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download_img(save_file, img_url):
    req = urllib.request.urlopen(img_url)
    content = req.read()
    with open(save_file, "wb") as f:
        f.write(content)


def main():
    gevent.joinall([
        gevent.spawn(download_img, "/home/haunis/Desktop/1.png",
                     "https://desk-fd.zol-img.com.cn/t_s640x530c5/g3/M01/0B/0B/ChMlWF7xhc2IYkHIABNkknpvnzUAAVIxgJnBXoAE2Sq374.jpg"),
        gevent.spawn(download_img, "/home/haunis/Desktop/2.png",
                     "https://desk-fd.zol-img.com.cn/t_s960x600c5/g4/M05/00/0E/ChMly170KFCIR1DXAD2iekbrjdQAAYR6AGITlkAPaKS329.jpg")
    ])


if __name__ == "__main__":
    main()
