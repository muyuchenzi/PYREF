"""
坐标转换
常用的三种坐标系间经纬度的相互转换
加密：wgs84 -> gcj02, gcj02 -> bd09
解密：gcj02 -> wgs84, bd09 -> gcj02
由于加密过程中的一些函数不存在反函数，所以解密的过程不存在解析解，只能用数值逼近的方式估计数值解，当迭代的次数趋于无穷时，数值解趋于真实值
wgs84 -> bd09 和 bd09 -> wgs84 这两种转换分两步进行

coord_transform支持点线面任何类型的地理图形转换
"""


import math
import numpy as np
import pandas as pd
import geojson.utils
from shapely.geometry import shape
from shapely.geometry import mapping

a = 6378245.0  # 克拉索夫斯基椭球参数长半轴a
ee = 0.00669342162296594323  #克拉索夫斯基椭球参数第一偏心率平方
PI = 3.14159265358979324  # 圆周率


class SRS():
    """固定支持的srs"""
  # 高德
    gcj02 = 'gcj02'
  # wgs84 +init=epsg:4326
    wgs84 = 'wgs84'
  # 百度
    bd09 = 'bd09'


def _transform(lon, lat, func, N, precision):
  lon0, lat0 = lon.copy(), lat.copy()
  def it(lon, lat, flag=1):
    mlon, mlat = func(lon, lat)
    dlon = lon0 - mlon
    dlat = lat0 - mlat
    lon += dlon
    lat += dlat
    if ((abs(dlon) < precision).all() and (abs(dlat) < precision).all()) or flag >= N:
      return lon, lat
    else:
      return it(lon, lat, flag + 1)
  return it(lon, lat)


def WGStoGCJ(lon, lat):
  """
  WGS坐标转换至GCJ02坐标
  Args:
    lon: np.array
    lat: np.array
  """

  x = lon - 105
  y = lat - 35

  dx = 300 + x + 2 * y + 0.1 * x ** 2 + 0.1 * x * y + 0.1 * abs(x) ** 0.5
  dx += (20 * np.sin(6 * x * PI) +
               20 * np.sin(2 * x * PI)) * 2 / 3
  dx += (20 * np.sin(x * PI) +
               40 * np.sin(x / 3 * PI)) * 2 / 3
  dx += (150 * np.sin(x / 12.0 * PI) +
               300 * np.sin(x / 30 * PI)) * 2 / 3

  dy = -100 + 2 * x + 3 * y + 0.2 * y ** 2 + 0.1 * x * y + 0.2 * abs(x) ** 0.5
  dy += (20 * np.sin(6 * x * PI) +
               20 * np.sin(2 * x * PI)) * 2 / 3
  dy += (20 * np.sin(y * PI) +
               40 * np.sin(y / 3 * PI)) * 2 / 3
  dy += (160 * np.sin(y / 12 * PI) +
               320 * np.sin(y * PI / 30)) * 2 / 3

  rady = lat * PI / 180
  magic = -np.sin(rady) ** 2 * ee + 1

  dx = dx * 180 / (a / magic ** 0.5 * np.cos(rady) * PI)
  dy = dy * 180 / (
      (a * (1 - ee)) / (magic * magic ** 0.5) * PI)

  return lon + dx, lat + dy


def GCJtoWGS(lon, lat, precision=1e-6, N=5):
  """
  GCJ02坐标转换至WGS坐标
  precision控制精度, N控制迭代次数; 至少指定一个, 同时指定时, 精度优先
  Args:
    lon: np.array
    lat: np.array
    precision: float
    N: integer
  """
  assert precision or N

  lon_WGS = lon.copy()
  lat_WGS = lat.copy()

  if not precision:
    for _ in range(N):
      mlon, mlat = WGStoGCJ(lon_WGS, lat_WGS)
      lon_WGS += lon - mlon
      lat_WGS += lat - mlat
    return lon_WGS, lat_WGS
  else:
    return _transform(lon_WGS, lat_WGS, WGStoGCJ, N, precision)


def GCJtoBD(lon, lat):
  """
  GCJ02坐标转换至BD09坐标
  Args:
    lon: np.array
    lat: np.array
  """
  _pi = PI * 3000 / 180
  z = (lon**2 + lat**2)**0.5 + 0.00002 * np.sin(lat * _pi)
  theta = np.arctan2(lat, lon) + 0.000003 * np.cos(lon * _pi)
  lon_BD = z * np.cos(theta) + 0.0065
  lat_BD = z * np.sin(theta) + 0.006
  return lon_BD, lat_BD


def BDtoGCJ(lon, lat, precision=1e-6, N=5):
  """
  BD09坐标转换至GCJ02坐标
  precision控制精度, N控制迭代次数; 至少指定一个, 同时指定时, 精度优先
  Args:
    lon: np.array
    lat: np.array
    precision: float
    N: integer
  """
  assert precision or N

  lon_GCJ = lon.copy()
  lat_GCJ = lat.copy()

  if not precision:
    for _ in range(N):
      mlon, mlat = GCJtoBD(lon_GCJ, lat_GCJ)
      lon_GCJ += lon - mlon
      lat_GCJ += lat - mlat
    return lon_GCJ, lat_GCJ
  else:
    return _transform(lon_GCJ, lat_GCJ, GCJtoBD, N, precision)


def WGStoBD(lon, lat):
  """
  WGS坐标转换至BD09坐标
  precision控制精度, N控制迭代次数; 至少指定一个, 同时指定时, 精度优先
  Args:
    lon: np.array
    lat: np.array
    precision: float
    N: integer
  """
  lon_GCJ, lat_GCJ = WGStoGCJ(lon, lat)
  return GCJtoBD(lon_GCJ, lat_GCJ)


def BDtoWGS(lon, lat, precision=1e-6, N=5):
  """
  WGS坐标转换至BD09坐标
  Args:
    lon: np.array
    lat: np.array
  """
  lon_GCJ, lat_GCJ = BDtoGCJ(lon, lat, precision=precision, N=N)
  return GCJtoWGS(lon_GCJ, lat_GCJ, precision=precision, N=N)


def _out_of_china(lgt, lat):
    """
        判断是否在国内
        只有国内的地图需要偏移
        :param lgt: WGS84坐标系的经度
        :param lat: WGS84坐标系的纬度
        :return: 不在国内返回True，在国内返回False
    """
    return not ((73.66 < lgt < 135.05) and (3.86 < lat < 53.55))

def _transform_lgt(lgt, lat):
    ret = 300.0 + lgt + 2.0 * lat + 0.1 * lgt * lgt + 0.1 * lgt * lat + 0.1 * math.sqrt(math.fabs(lgt))
    ret += (20.0 * math.sin(6.0 * lgt * math.pi) + 20.0 * np.sin(2.0 * lgt * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lgt * math.pi) + 40.0 * math.sin(lgt / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lgt / 12.0 * math.pi) + 300.0 * math.sin(lgt / 30.0 * math.pi)) * 2.0 / 3.0
    return ret

def _transform_lat(lgt, lat):
    ret = -100 + 2 * lgt + 3 * lat + 0.2 * lat * lat + 0.1 * lgt * lat + 0.2 * math.sqrt(math.fabs(lgt))
    ret += (20.0 * math.sin(6.0 * lgt * math.pi) + 20.0 * math.sin(2.0 * lgt * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * math.pi) + 40.0 * math.sin(lat / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * math.pi) + 320 * math.sin(lat * math.pi / 30.0)) * 2.0 / 3.0
    return ret

def wgs84_to_gcj02_point(gps_lgt, gps_lat):
    """
    WGS84(原始的GPS经纬度坐标)  ->  GCJ02(火星坐标系)
    单点的坐标转换

    :param gps_lgt: [float] WGS84坐标系的经度
    :param gps_lat: [float] WGS84坐标系的纬度
    :return:
        [lgt, lat] （即 [GCJ02坐标系的经度, GCJ02坐标系的纬度]）
        数据类型 [float, float]
    """
    a = 6378245.0
    ee = 0.00669342162296594323

    if _out_of_china(gps_lgt, gps_lat):
        return gps_lgt, gps_lat

    dLgt = _transform_lgt(gps_lgt - 105, gps_lat - 35)
    dLat = _transform_lat(gps_lgt - 105, gps_lat - 35)
    radLat = gps_lat * math.pi / 180
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLgt = (dLgt * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
    lgt = gps_lgt + dLgt
    lat = gps_lat + dLat

    return [lgt, lat]


# TODO 考虑加入精度控制，当前后两次迭代结果的差小于e-6时，停止迭代
def gcj02_to_wgs84_point(gcj_lgt, gcj_lat, N=5):
    """
    GCJ02(火星坐标系)  ->  WGS84(原始的GPS经纬度坐标)
    单点的坐标转换

    :param gcj_lgt: [float] GCJ02坐标系的经度
    :param gcj_lat: [float] GCJ02坐标系的纬度
    :param N: 迭代次数，默认为10次
        按照博客http://blog.51cto.com/zhangchanggong/1547863中的算法，
        当迭代次数 -> 无穷时，估计结果 -> 原始的真实gps坐标
    :return:
        [lgt, lat] （即 [WGS84坐标系的经度, WGS84坐标系的纬度]）
        数据类型 [float, float]
    """
    lgt, lat = gcj_lgt, gcj_lat
    for i in range(N):
        mglgt, mglat = wgs84_to_gcj02_point(lgt, lat)
        lgt += gcj_lgt - mglgt
        lat += gcj_lat - mglat

    return [lgt, lat]


def gcj02_to_bd09_point(gcj_lgt, gcj_lat):
    """
    GCJ02(火星坐标系)  ->  BD-09(百度坐标系)
    单点的坐标转换

    :param gcj_lgt: [float] GCJ02坐标系的经度
    :param gcj_lat: [float] GCJ02坐标系的纬度
    :return:
        [lgt, lat] （即 [BD09坐标系的经度, BD09坐标系的纬度]）
        数据类型 [float, float]
    """
    x_pi = math.pi * 3000 / 180
    z = math.sqrt(gcj_lgt * gcj_lgt + gcj_lat * gcj_lat) + 0.00002 * math.sin(gcj_lat * x_pi)
    theta = math.atan2(gcj_lat, gcj_lgt) + 0.000003 * math.cos(gcj_lgt * x_pi)
    lgt = z * math.cos(theta) + 0.0065
    lat = z * math.sin(theta) + 0.006

    return [lgt, lat]


# TODO 考虑加入精度控制，当前后两次迭代结果的差小于e-6时，停止迭代
def bd09_to_gcj02_point(bd_lgt, bd_lat, N=5):
    """
    BD-09(百度坐标系)  ->  GCJ02(火星坐标系)
    单点的坐标转换

    :param bd_lgt: [float] BD-09坐标系的经度
    :param bd_lat: [float] BD-09坐标系的纬度
    :param N: 迭代次数，默认为10次
        按照博客http://blog.51cto.com/zhangchanggong/1547863中的算法，
        当迭代次数 -> 无穷时，估计结果 -> 加密前的gcj坐标
    :return:
        [lgt, lat] （即 [gcj02坐标系的经度, gcj02坐标系的纬度]）
        数据类型 [float, float]
    """
    lgt, lat = bd_lgt, bd_lat
    for i in range(N):
        mglgt, mglat = gcj02_to_bd09_point(lgt, lat)
        lgt += bd_lgt - mglgt
        lat += bd_lat - mglat

    return [lgt, lat]


def wgs84_to_bd09_point(gps_lgt, gps_lat):
    """
    WGS84(原始的GPS经纬度坐标)  ->  BD-09(百度坐标系)
    单点的坐标转换

    :param gps_lgt: [float] WGS84坐标系的经度
    :param gps_lat: [float] WGS84坐标系的纬度
    :return:
        [lgt, lat] （即 [BD-09坐标系的经度, BD-09坐标系的纬度]）
        数据类型 [float, float]
    """
    return gcj02_to_bd09_point(*wgs84_to_gcj02_point(gps_lgt, gps_lat))


def bd09_to_wgs84_point(bd_lgt, bd_lat):
    """
    BD-09(百度坐标系)  ->  WGS84(原始的GPS经纬度坐标)
    单点的坐标转换

    :param bd_lgt: [float] BD-09坐标系的经度
    :param bd_lat: [float] BD-09坐标系的纬度
    :param N: 迭代次数，默认为10次
        按照博客http://blog.51cto.com/zhangchanggong/1547863中的算法，
        当迭代次数 -> 无穷时，估计结果 -> 加密前的gcj坐标
    :return:
        [lgt, lat] （即 [gcj02坐标系的经度, gcj02坐标系的纬度]）
        数据类型 [float, float]
    """
    return gcj02_to_wgs84_point(*bd09_to_gcj02_point(bd_lgt, bd_lat))


_fn_mapping = {
    (SRS.bd09, SRS.wgs84): bd09_to_wgs84_point,
    (SRS.gcj02, SRS.wgs84): gcj02_to_wgs84_point,
    (SRS.wgs84, SRS.bd09): wgs84_to_bd09_point,
    (SRS.gcj02, SRS.bd09): gcj02_to_bd09_point,
    (SRS.wgs84, SRS.gcj02): wgs84_to_gcj02_point,
    (SRS.bd09, SRS.gcj02): bd09_to_gcj02_point
}


def coord_transform_single_point(lng: float, lat: float, from_srs: SRS, to_srs: SRS):
    """坐标系转换

    :param lng: 输入的经度
    :param lat: 输入的纬度
    :param from_srs: 输入坐标的格式
    :param to_srs: 输出坐标的格式
    """
    if from_srs == to_srs:
        return lng, lat

    if pd.isnull(lng) or pd.isnull(lat):
        return None, None

    key = (from_srs, to_srs)
    if key not in _fn_mapping:
        raise NotImplementedError('not support transformation from %s to %s' %
                              (from_srs, to_srs))
    lng, lat = _fn_mapping[key](lng, lat)
    return lng, lat

def coord_transform_geojson(obj: dict, from_srs: SRS, to_srs: SRS):
    """对GeoJSON格式内的所有坐标点执行坐标系转换"""
    return geojson.utils.map_tuples(
        lambda c: coord_transform_single_point(c[0], c[1], from_srs, to_srs),
        obj
    )

def coord_transform(geometry, from_srs: SRS, to_srs: SRS):
    """将shapely.geometry转化为Geojson格式执行坐标转换，再返回为shapely.geometry"""
    return shape(coord_transform_geojson(mapping(geometry), from_srs, to_srs))
