import geopandas as gpd
import ogr
import json

bo = gpd.read_file(r'E:\李震祥\PYGIT\PYref\ReviewCode\geopandas\一轴三带3D\data\静安区边界.shp', encoding='utf-8')
bo['Floor'] = 2
bo['region_name'] = bo['name']
bo = bo[['name', 'Floor', 'region_name', 'geometry']]
bo.to_file(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\temp\静安区边界.shp', encoding='utf-8')

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r"D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\temp\静安区边界.shp"
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
}

lyr = data_source.GetLayer(0)
for feature in lyr:
    fc['features'].append(feature.ExportToJson(as_object=True))

jsFile = json.dumps(fc)

with open(r'D:\李震祥\code\code\静安发改委_adimin\一轴三带3D\result\静安区边界.js', 'w') as f:
    f.write('var region_jingan =  ' + jsFile)

import geopandas as gpd

gdf = gpd.read_file(shp_path)
