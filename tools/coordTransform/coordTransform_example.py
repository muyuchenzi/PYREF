import geopandas as gpd
import pandas as pd
import numpy as np
from src.coordTransform import coord_transform
from src.coordTransform import WGStoBD, BDtoWGS, GCJtoWGS
from shapely.geometry import Point, LineString, Polygon

if __name__ == '__main__':
    
    ########### single test ###################################################
    geom = Point(121,31)
    geom = LineString([(120,30),(121,31)])
    geom = Polygon([(120,30),(121,31),(120,31),(120,30)])  
    
    print(coord_transform(geom, from_srs='wgs84', to_srs='bd09'))
    print(coord_transform(geom, from_srs='gcj02', to_srs='bd09'))
    print(coord_transform(geom, from_srs='bd09', to_srs='wgs84'))
    print(coord_transform(geom, from_srs='gcj02', to_srs='wgs84'))
    print(coord_transform(geom, from_srs='wgs84', to_srs='gcj02'))
    print(coord_transform(geom, from_srs='bd09', to_srs='gcj02'))
    
    ########### df trans test #################################################

