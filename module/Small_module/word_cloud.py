import random
import numpy as np
from numpy.random import randint
from operator import add, sub
import json
import operator
from math import ceil
import os
import wordcloud
import pandas as pd
import matplotlib.pyplot as plt


def temp(n):
    df = pd.read_excel(r'E:\李震祥\PYGIT\Temp\data\各省市订单数据origin.xlsx')
    df = df[['省']]
    word = ','.join(x for x in df['省'] if x != [])
    wc = wordcloud.WordCloud(
        background_color="green",  # 背景颜色"green"绿色
        max_words=100,  # 显示最大词数
        font_path='./fonts/simhei.ttf',  # 显示中文
        min_font_size=5,
        max_font_size=40,
        width=1200  # 图幅宽度

    )
    plt.imshow(wc)
    plt.show()
    res = wc.generate(word)
    res.to_file(r'E:\李震祥\PYGIT\Temp\result\word_cloud.png')


def main():
    xx = temp(30)
    print(list(xx))


if __name__ == "__main__":
    main()
