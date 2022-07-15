import geopandas as gpd
import shapely
from shapely import geos
from shapely.geometry import Point
from sqlalchemy import create_engine
from shapely import wkb
import pandas as pd
import re
import numpy as np
import ogr
import json
import simplejson

bo = pd.read_excel(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\data\静安边界_一轴三带.xlsx', encoding='utf-8')
bo['geometry'] = bo['geometry'].apply(lambda x: wkb.loads(x, hex=True))

bo = gpd.GeoDataFrame(bo, geometry='geometry', crs={'init': 'epsg:4326'})
bo.rename(columns={'名称': 'name', '一轴三带': 'building_name'}, inplace=True)
bo['name'] = range(1, bo.shape[0] + 1)

bo['building_name'].fillna(value=" ", inplace=True)
# 给一轴三带加上一个
for i in range(bo.shape[0]):
    if bo.loc[i, 'building_name'] == '复合发展主轴':
        bo.loc[i, 'Floor'] = 4;
    else:
        bo.loc[i, 'Floor'] = 2

bo = bo[['name', 'Floor', 'building_name', 'geometry']]

# 建筑面数据修改合并
bo.to_file(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\一轴三带.shp', encoding='utf-8')

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r"D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\一轴三带.shp"
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
}

lyr = data_source.GetLayer(0)
for feature in lyr:
    fc['features'].append(feature.ExportToJson(as_object=True))

jsFile = json.dumps(fc)

with open(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\一轴三带.js', 'w') as f:
    f.write('var building =  ' + jsFile)
