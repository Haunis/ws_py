"""
安装jieba:
    pip3 install jieba
安装wordcloud:
    pip3 install wordcloud

"""
import numpy as np
import matplotlib.pyplot as plt
import jieba  # 分词软件
from wordcloud import WordCloud, STOPWORDS
import PIL.Image as image


def get_word_cn(file):  # 中文,使用jieba; 返回分好词的txt
    f = open(file)
    file_content = f.read()
    word_list = jieba.cut(file_content)  # 返回generator
    text = ' '.join(word_list)  # 在生成器yield返回的str后面添加' '
    return text


def get_word_eng(file):  # 英文,直接返回内容即可;并未使用jieba
    f = open(file)
    file_content = f.read()
    return file_content


def show_word_cloud(text):
    img_mask = np.array(image.open('img_heart.jpg'))  # 加入背景形状
    # 生成词云
    wordcloud = WordCloud(background_color="white",
                          font_path='/usr/share/fonts/consolas/YaHeiConsolas.ttf',
                          mask=img_mask, stopwords=STOPWORDS).generate(text)
    plt.imshow(wordcloud)  # 显示词云图
    plt.axis("off")  # 不显示坐标轴
    plt.show()


if __name__ == '__main__':
    text = get_word_cn('word_cn.txt')
    # text = get_word_eng('word_eng.txt')
    show_word_cloud(text)
