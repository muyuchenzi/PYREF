# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:35:17 2018

@author: zzz
"""
import re
import sys
import hashlib
import requests
import pandas as pd
from shapely import wkb
from shapely.geometry import shape

class DmapHandler():
    
    base_url = 'http://www.maicedata.com/datamap'
    login_api = '/auth/login'
    app_role_api = '/auth/user/role'
    data_list_api = '/auth/user/data'
    group_api = '/auth/group'
    group_app_role_api = '/auth/entityinfo/group_role'
    get_private_data_api = '/upload/query'
    get_private_data_info_api = '/data/customer'
    upload_private_data_api = '/upload/modify'
    delete_private_data_api = '/upload/modify'
    create_user_api = '/auth/user'
    group_api = '/auth/group'
    vault_api = '/vault'
    
    def __init__(self, username, password):
        '''
        attribute list:
            
            username 登录名
            password 登录密码
            token    查询所用token
            headers  包含token 用于requests包的headers
            user_id  用户在datamap中的唯一用户id
            app_info 用户所有app的结果
            app_name 用户所属默认app名
            app_id   用户所属默认app id
            app_menu 用户所属默认app的功能dic
            app_role 用户所属默认app的角色代码dic
                     一般为{'user': roleid, 'admin': roleid}的形式
                     创建用户时需填入roleid
            group_info 所有群组的结果
            group_id 用户所属第一个群组的id
            group_name 用户所属第一个群组的名称
            group_user_level 用户在第一个群组内的等级（管理员,高,中,低）
            group_level 用户所属第一个群组的等级对应id dic
                        一般为 {'低': id, '高': id ,...}
                        修改群组时需填入levelid
            data_list 可看可修改数据表 pandas.DataFrame
                      维度有 geom_type, object_type, package_id, modifyOrRead
                      其中 geom_type, object_type对应function中上传及读表的参数
                      
        function list:
            
            getPrivateData 读取datamap中的私有数据
                输入 data_list中的表名 object_type，地理类型 geom_type
                返回 pandas.DataFrame
                地理数据统一置于 geometry字段内
                若无该表 返回空值
                
            uploadPrivateData 上传数据至datamap中的私有数据 
                              可用于append数据或直接新建数据包
                              需替换数据 请先delePrivateData删除原数据再上传
                输入 dataframe，私有数据包名 object_type，地理类型 geom_type
                需经 检查-转换-上传 三个步骤
                上传前请确认 dataframe 是否有 name 字段, 且 name 字段类型是否为 str
                如果是地理数据 请确认是否有 geometry 字段，且为shapely.geometry类型
                若上传完成 会打出若干个 {"status":"success",...} 的json
            
            delePrivateData 删除私有数据
                输入 data_list中的表名 object_type，地理类型 geom_type，以及需要删除的行id list
                如果要删除整表，不输入id list即可
                
            grantData2Group 将数据权限赋予群组
                输入 data_list中的表名 object_type，地理类型 geom_type，以及group_id
                group_id 即为 .group_info 中各个元素的'id'属性
                如不填入group_id，则视群组为该账号的第一个群组
                
            deleData4Group 将数据权限从群组中删除
                输入 data_list中的表名 object_type，地理类型 geom_type，以及group_id
                group_id 即为 .group_info 中各个元素的'id'属性
                如不填入group_id，则视群组为该账号的第一个群组                
        
        备注：
            geom_type 可填项为 plain/point/line/polygon
            object_type 即为私有数据的表名，可通过 .data_list 查看
        '''
        self.username = username
        self.password = password
        self.getAuthToken()
        self.getHeaders()
        self.getAppRole()
        self.getGroupInfo()
        self.getDataList()

    def sting2md5(self, string):
        '将字符串转为md5码'
        m = hashlib.md5()
        m.update(bytes(string, encoding='utf-8'))
        return m.hexdigest()

    def getAuthToken(self):
        '获取登录后的token及相关信息'
        # 密码需经md4进行加密
        user_pass = {
            "name": self.username,
            "password": self.sting2md5(self.password)
        }
        
        # 调用api
        login = requests.post(f'{self.base_url}{self.login_api}', 
                              json = user_pass)
        login_res = login.json()
        
        # 记录基础信息
        if login_res['rc'] != 0:
            print('登陆失败，请检查用户名或密码！')
            sys.exit()
        else:
            self.token = login_res['result']['auth']
            self.user_id = login_res['result']['customer']['id']
            self.app_info = login_res['result']['apps']['all']
            self.app_name = login_res['result']['apps']['default']['name']
            self.app_id = login_res['result']['apps']['default']['id']
            self.app_menu = login_res['result']['apps']['default']['detail_menu']

    def getHeaders(self):
        '获取用于requests的headers'
        self.headers = {'Authorization': self.token}

    def getAppRole(self):
        '获取app的role'
        # 调用api
        r = requests.get(f'{self.base_url}{self.app_role_api}', 
                         headers=self.headers)
        role_dic = {}
        for one_role in r.json()['result']:
            role_dic[one_role['name']] = one_role['id']
        
        self.app_role = role_dic
    
    def getGroupInfo(self):
        '获取用户所在群组信息'
        # 调用api
        r = requests.get(f'{self.base_url}{self.group_api}',
                         headers=self.headers)
        self.group_info = r.json()['result']
        
        # 如果有所在群组的话
        if len(self.group_info) > 0:
            self.group_name = self.group_info[0]['name']
            self.group_id = self.group_info[0]['id']
            self.group_user_level = self.group_info[0]['level_name']
        
            # 所在群组的level id
            r = requests.get(f'{self.base_url}{self.group_app_role_api}', 
                             headers=self.headers)
            self.group_level = {}
            for onelevel in r.json()['result']:
                self.group_level[onelevel['name']] = onelevel['id']
        # 无群组 皆为空
        else:
            self.group_name = None
            self.group_id = None
            self.group_user_level = None
            self.group_level = None
    
    def getDataList(self):
        '获取用户可看可修改数据列表'
        # 调用api
        data = {'group_id': self.group_id}
        r = requests.get(f'{self.base_url}{self.data_list_api}',
                         data = data,
                         headers=self.headers)        
        data_list = r.json()['result']
        del data_list['admin']
        
        # str to dic
        modify = [self.splitDataInfo(data) for data in data_list['can_modify']]
        read   = [self.splitDataInfo(data) for data in data_list['can_read']]
        columns= ["package_id","geom_type","object_type"]
        self.data_list = pd.concat([pd.DataFrame(modify, columns=columns).assign(modifyOrRead='modify'),
                                    pd.DataFrame(read, columns=columns).assign(modifyOrRead='read')])
    
    def updateDataList(func):
        """
        运行函数后 重新获取data_list表
        """
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.getDataList()
        return wrapper

    def checkInGroup(func):
        """
        运行函数后 检查账号是否属于群组内，如没有，发出提示，不执行与群组相关的命令
        """
        def wrapper(self, *args, **kwargs):
            if self.group_name is not None:
                func(self, *args, **kwargs)
            else:
                print("该账号无群组，请先添加群组后执行群组操作！")
        return wrapper
    
    def getPrivateData(self, object_type, geom_type, page_size=None, page_num=None):
        '''
        获取私有数据转换为 dataframe
        输入为self.data_list中的geom_type字符串及object_type字符串
        返回为pandas.dataframe, 如有geometry则已转换为shapely格式
        page_num默认从0开始
        page_size默认100，最大100
        '''
        
        if any(list((self.data_list['geom_type']==geom_type) &
                    (self.data_list['object_type']==object_type))):
            
            if (page_size is not None) & (page_num is not None): 
                data = {'geo_type': geom_type,
                        'check_geometry': False,
                        'page_size': page_size,
                        'page_num': page_num,
                        'attr': 'address'}
            else:
                data = {'geo_type': geom_type,
                        'check_geometry': False,
                        'attr': 'address'}
                
            json = {'object_types': [object_type],
                    'filters': []}
        
            r = requests.post(f'{self.base_url}{self.get_private_data_api}',
                              headers=self.headers, 
                              params=data,
                              json=json)       
            return self.dmapData2Df(r.json()['result'])     
        
        else:
            print('该表格不存在！返回空值')
            return None

    @updateDataList
    def uploadPrivateData(self, df_ori, object_type, geom_type):
        '''
        将dataframe上传到datamap
        需经 检查-转换-上传 三个步骤
        最后更新数据列表
        '''

        # 检查
        df = df_ori.copy()
        df = self.checkUploadData(df, object_type, geom_type)
        row_num = df.shape[0]

        # 转换和上传
        if row_num <= 1000:
            self.uploadPrivateDataBase(df)
        else:
            start_num = 0
            while start_num < row_num:
                if (start_num + 1000 > row_num):
                    self.uploadPrivateDataBase(df.iloc[start_num: row_num])
                else:
                    self.uploadPrivateDataBase(df.iloc[start_num: (start_num+1000)])
                start_num += 1000
                
    @updateDataList
    def delePrivateData(self, object_type, geom_type, ids=None):
        '''
        从私有数据中删除记录
        输入为self.data_list中的geom_type字符串及object_type字符串
        ids为需要删除的 id list，为None时自动删除所有数据
        '''
        if ids is None:
            privateData = self.getPrivateData(object_type, geom_type)
            ids = list(privateData['id'])
            del privateData
        
        json = {"ids": ids, "object_type": object_type, "geometry_type": geom_type}
        
        r = requests.delete(f'{self.base_url}{self.delete_private_data_api}', 
                            headers=self.headers, 
                            json=json)
        print(r.text)
        
    @checkInGroup
    def grantData2Group(self, object_type, geom_type, group_id=None):
        '''
        将数据权限赋予群组
        group_id 即为 .group_info 中各个元素的'id'属性
        如不填入group_id，则视群组为该账号的第一个群组
        '''
        if group_id is None:
            group_id = self.group_id
        
        json = {"object_types":[{"geom_type": geom_type,
                                 "object_type": object_type}],
                "pages": []}
                
        r = requests.post(f'{self.base_url}{self.group_api}/{group_id}/data',
                          headers=self.headers,
                          json=json)
        print(r.text)

    @checkInGroup
    def deleData4Group(self, object_type, geom_type, group_id=None):
        '''
        将数据权限从群组中删除
        group_id 即为 .group_info 中各个元素的'id'属性
        如不填入group_id，则视群组为该账号的第一个群组
        '''
        if group_id is None:
            group_id = self.group_id
        
        json = {"object_types":[{"geom_type": geom_type,
                                 "object_type": object_type}]}
                
        r = requests.delete(f'{self.base_url}{self.group_api}/{group_id}/data',
                            headers=self.headers,
                            json=json)
        print(r.text)

    def getMediaInfo(self):
        '''
        获取多媒体数据详情
        '''                
        params = {"types": "files,js_graph,link", "detail": True}
        
        r = requests.get(f'{self.base_url}{self.vault_api}',
                         headers=self.headers,
                         params=params)
        print(r.text)  
        
    def uploadPrivateDataBase(self, df):
        '''
        上传数据到datamap的基础功能
        '''
        dmapUpload = self.df2DataMap(df)
        
        for json in dmapUpload:
            r = requests.post(f'{self.base_url}{self.upload_private_data_api}',
                              headers = self.headers,
                              params = {'force': True},
                              json = json)  
            print(r.text)       
            
    def dmapData2Df(self, rlt):
        '''
        将返回值转换为 dataframe
        '''
        def onerowHandler(row):
            thel = row['extra']
            thel['object_type'] = row['object_type']
            thel['name'] = row['name']
            thel['id'] = row['id']
            thel['geometry'] = row['geometry']
            thel["address"] = row["address"]
            
            return thel
        
        data_list = [onerowHandler(row) for row in rlt]
        df = pd.DataFrame(data_list)
        
        if (df.iloc[0]['geometry'] is None):
            df = df.drop(columns='geometry')
            print('无地理信息表')
            pass
        else:
            df.loc[:,'geometry'] = df['geometry'].apply(shape)
        
        return df    
    
    def df2DataMap(self, df):
        '''
        将dataframe转换为columns和values
        '''
        # 获取所有缺失值组合的可能
        allDataMapUploadTypes = list(df.apply(lambda x: x.isna(), axis=1)\
                                       .drop_duplicates()\
                                       .apply(lambda x: x.tolist(), axis=1))
       
        # 每个缺失值组合提取成一个dataframe 转换为json
        dmapUpload = []
        for onetype in allDataMapUploadTypes:
            
            onecols = [x for x in range(len(onetype)) if not onetype[x]]
            oneUpload = df.loc[df.apply(lambda x: list(x.isna())==onetype,axis=1),:]\
                          .iloc[:, onecols]
                          
            cols = list(oneUpload.columns)
            values = list(oneUpload.apply(lambda x: list(x), axis=1))
            
            dmapUpload.append({"columns": cols, "values": values})
        
        return dmapUpload

    def splitDataInfo(self, infoStr):
        '将数据信息字符串转为dic'
        infoStr = infoStr.split(',')
        return [int(infoStr[0]), infoStr[1], infoStr[2]]

#    def createUser(self, name, email, area_code=86, if_admin=False, enable = True,
#                   detail_menu=None, phone=None):
#        '''
#        新建用户 至少需要输入 用户名和email
#        '''
#        # 默认功能与原账号一致
#        if detail_menu is None:
#            detail_menu = self.app_menu
#        
#        # 新建用户是否为app管理员
#        if if_admin:
#            admin = [{"app_id": self.app_id, "role_id": self.app_role['admin']}]
#        else:
#            admin = [{"app_id": self.app_id, "role_id": self.app_role['user']}]
#        
#        # 创建json
#        user_dic = {
#            "email": email, "enable": enable,
#            "area_code": area_code, "name": name,
#            "admin": admin, "detail_menu": detail_menu
#        }
#        
#        if phone is not None:
#            user_dic['phone'] = str(phone)
#        
#        self.createUserBase(user_dic)
#
#    def createUserBase(self, user_dic):
#        '''
#        新建用户基础功能
#        '''
#        r = requests.post(f'{self.base_url}{self.create_user_api}',
#                          headers=self.headers,
#                          json=user_dic)
#        print(r.json())

    def checkUploadData(self, df, object_type, geom_type):
        '''
        检查上传数据的完整性
        检查项包括
            是否包含name字段
            是否包含id字段，如果有自动删除
            如果私有数据中已有 object_type 表名
                是否符合原数据格式
                是否name没有重复
            geom_type有四种选择 plain/point/line/polygon, plain表示非地理数据
            如果geom_type为plain, 不需要有geometry列
            如果geom_type不为plain，是否有一列为geometry且为shapely.geometry类型
            
            如果geom_type为point，函数将geometry转化为lng lat字段
            如果geom_type为其他，函数将geometry列转为ewkb格式字符串
            添加object_type, geometry_type字段
        '''
        df_cols = list(df.columns)
        
        # 是否包含name字段
        if 'name' not in df_cols:
            if '名称' not in df_cols:
                print('上传数据不包含name字段，停止上传！')
                sys.exit()
            else:
                df = df.rename(columns={"名称":"name"})
                df_cols = list(df.columns)
        
        if any([col in df_cols for col in ['名称','地址','经度','纬度']]):
            print("上传数据不得包含 名称/地址/经度/纬度 字段, 停止上传！")
            sys.exit()
        
        # 是否包含id字段
        if 'id' in df_cols:
            df = df.drop(columns='id')
        
        # 如果 geom_type不为规定字符，不能上传
        if (geom_type not in ['plain', 'point', 'line', 'polygon']):
            print('上传数据类型只能为 plain/point/line/polygon，停止上传！')
            sys.exit()
        
        # 如果 geom_type为plain，不能有geometry字段
        if (geom_type=='plain') & ('geometry' in df_cols):
            print('上传数据不包含地理数据，不能包含geometry字段，停止上传！')
            sys.exit()
            
        # 如果 geom_type为其他，必须有geometry字段
        if (geom_type in ['point', 'line', 'polygon']) & ('geometry' not in df_cols):
            print('上传数据需包含地理数据，未检测到geometry字段，停止上传！')
            sys.exit()
            
        # 如果 geom_type为point，geometry字段需转化为lng,lat字段
        if (geom_type=='point'):
            df.loc[:,'lng'] = df['geometry'].apply(lambda x: str(x.x))
            df.loc[:,'lat'] = df['geometry'].apply(lambda x: str(x.y))
            df = df.drop(columns='geometry')
            
        # 如果 geom_type为line或polygon，geometry字段需转化为ewkb格式
        if (geom_type in ['line', 'polygon']):
            df.loc[:,'geometry'] = df['geometry'].apply(lambda x: wkb.dumps(x,hex=True,srid=4326))
        
        # 如果 数据中已有相关表格，检查其余字段是否一致
        if any(list((self.data_list['geom_type']==geom_type) &
                    (self.data_list['object_type']==object_type) &
                    (self.data_list['modifyOrRead']=='modify'))):
            
            sample = self.getPrivateData(object_type, geom_type)
            sample_cols = list(sample.columns)
            sample_names = list(sample['name'])
            del sample
            
            # 必选项不用检查
            for del_col in ['geometry','id','object_type','name', 'lng', 'lat']:
                if del_col in sample_cols:
                    sample_cols.remove(del_col)
                if del_col in df_cols:
                    df_cols.remove(del_col)

            # 检查其余字段是否一致
            if all(elem in sample_cols for elem in df_cols) & (len(df_cols)==len(sample_cols)):
                print('')
                pass
            else:
                print('字段不一致！\n样例字段如下:\n')
                print(sample_cols)
                print('\n上传字段如下:\n')
                print(df_cols)
                sys.exit()
                
            # 检查name是否有重复
            df.loc[:,'name'] = self.checkDuplicateName(list(df['name']), sample_names)
        else:
            df.loc[:,'name'] = self.checkDuplicateName(list(df['name']), [])
        
        # 添加相关字段
        df.loc[:,'geometry_type'] = geom_type
        df.loc[:,'object_type'] = object_type
        
        # 去除所有行皆为None的行
        df = df[df.apply(lambda x: all(list(x.isna()))==False, axis=1)]
        
        return df
    
    def checkDuplicateName(self, name_list, record_names):
        '''
        比较两组名称，对重复的名称做后面加上 (\d) 的修改
        返回修改后的名称组
        若自检是否重复，record_names=[]即可
        '''
        # 建立名称池
        record_dic = {}
        record_pattern = re.compile('^(.+) \((\d+)\)$')

        for record in record_names:
            # 取得 真实name 与 number 
            if record_pattern.match(record) is not None:
                name = record_pattern.sub('\\1', record)
                number = int(record_pattern.sub('\\2', record))
            else:
                name = record
                number = 0
            
            # 更新 record_dic
            if name in record_dic.keys():
                # 更新 max_num
                max_num = record_dic[name]['max']
                if number > max_num:
                    record_dic[name]['max'] = number
                # 更新 records
                record_dic[name]['records'].append(record)
                
            elif name not in record_dic.keys():
                # 
                record_dic[name] = {'max': number,
                                    'records': [record]}

        for i in range(len(name_list)):
            todo_name = name_list[i]
            
            # 取得 真实name 与 number 
            if record_pattern.match(todo_name) is not None:
                name = record_pattern.sub('\\1', todo_name)
                number = int(record_pattern.sub('\\2', todo_name))
            else:
                name = todo_name
                number = 0            

            # 更新 
            if name in record_dic.keys():
                # 判断是否需要更新 name_list
                if todo_name in record_dic[name]['records']:
                    # 更新 name_list 且 max+1
                    record_dic[name]['max'] += 1
                    name_list[i] = f"{name} ({record_dic[name]['max']})"
                else:
                    # 只是更新 max
                    max_num = record_dic[name]['max']
                    if number > max_num:
                        record_dic[name]['max'] = number
                        
                record_dic[name]['records'].append(name_list[i])
                
            elif name not in record_dic.keys():
                # 只需更新 record_dic即可
                record_dic[name] = {'max': number,
                                    'records': [name_list[i]]}
            
        return name_list

if __name__ == '__main__':

    username = ''
    password = ''
    
    # 创建时输入用户名及密码
    pdfgw = DmapHandler(username, password)
    
    # 获取私有数据列表
    print(pdfgw.data_list.shape[0])
    
    # 读取数据
    df = pdfgw.getPrivateData('现有体育设施', 'point') 

    # 上传数据
    pdfgw.uploadPrivateData(df, '现有体育设施_testtest', 'point')
    print(pdfgw.data_list.shape[0])
    
    # 删除数据
    pdfgw.delePrivateData('现有体育设施_testtest', 'point')
    print(pdfgw.data_list.shape[0])
