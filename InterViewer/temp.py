import pandas as pd
import math
import string
import re
import geopandas as gpd

# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。传送带上的第 i 个包裹的重量为 weights[i]。每一天，
# 我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
#
#
# 示例 1 :weights = [1,2,3,4,5,6,7,8,9,10], D = 5 输出: 15  解释: 船舶最低载重 15 就能够在 5 天内送达所有包裹，
# 第 1 天：1, 2, 3, 4, 5 第 2 天：6, 7 第 3 天：8 第 4 天：9 第 5 天：10
# 示例 2 :[3,2,2,4,1,4] D ==3 输出: 6 解释：第 1 天：3, 2 第 2 天：2, 4 第 3 天：1, 4
# 示例 3 :weights = [1,2,3,1,1], D = 4 输出：3 解释：第 1 天：1 第 2 天：2 第 3 天：3 第 4 天：1, 1

import psycopg2


def solution():
    weights = input()  # [1,2,3,4,5,6,7,8,9,10]
    days = input()  # 5

    select_w = "select distin populution from shanghai_2010"
    psycopg2.connect()
    select_x = "select count(country) from shanghai_2010"
    # max_weight = max(weights)
    maxx = sum(weights)
    for i in range(maxx + 1):
        temp_list = []
        for j in range(len(weights)):
            start = null, = None, undefine


if __name__ == '__main__':
    solution()
