import pandas as pd
import ogr
import json
import geopandas as gpd
from shapely import wkb

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r"D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\data\上海市路网信息.shp"
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'GeometryCollection',
    'geometries': []
    }
lyr = data_source.GetLayer(0)
for feature in lyr:
    fc['geometries'].append(feature.ExportToJson(as_object=True))
jsFile = json.dumps(fc)
with open(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\上海路网信息.js', 'w') as f:
    f.write('var routes =  ' + jsFile)

