"""
设置要存储的路径和filemode打开方式即可(w：只写方式，a:追加方式)
其中filemode的含义和io流的文件打开方式含义一样
"""

import logging

logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
