import pandas as pd
from keplergl import KeplerGl
import json
import time

with open(
        r'E:\李震祥\GitHub\DataScienceStudyNotes\历史文章附件列表\（数据科学学习手札85）Python+Kepler.gl轻'
        r'松制作酷炫路径动画\geometry\geometry\重庆市渝中区_osm路网_道路.geojson', encoding='utf-8') as f:
    raw_road = json.load(f)

start_time = time.mktime(time.strptime('2020-05-29 20:00:00', "%Y-%m-%d %H:%M:%S"))
for i in range(raw_road['features'].__len__()):
    for j in range(raw_road['features'][i]['geometry']['coordinates'].__len__()):
        shift_time = int((j / raw_road['features'][i]['geometry']['coordinates'].__len__()) * 3600)
        raw_road['features'][i]['geometry']['coordinates'][j].extend([0, int(start_time) + shift_time])
from keplergl import KeplerGl

map1 = KeplerGl(height=500, data={"flow": raw_road})
map1.save_to_html(file_name='渝中区.html')
