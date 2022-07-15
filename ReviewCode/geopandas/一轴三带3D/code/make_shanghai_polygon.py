import geopandas as gpd
import ogr
import json
import pandas as pd

bo = gpd.read_file(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\data\上海市一轴三带与区县并集1.shp', encoding='utf-8')
# 突出显示静安 给静安加上一个高度
bo.rename(columns={'name_1':'name','Floor_1':'Floor'},inplace=True)
bo = bo[['name', 'Floor', 'building_n', 'geometry']]
bo.to_file(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\temp\区县边界与一轴三带并集.shp', encoding='utf-8')

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r"D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\temp\区县边界与一轴三带并集.shp"
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
}

lyr = data_source.GetLayer(0)
for feature in lyr:
    fc['features'].append(feature.ExportToJson(as_object=True))

jsFile = json.dumps(fc)

with open(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\上海区县与一轴三带1.js', 'w') as f:
    f.write('var region =  ' + jsFile)
