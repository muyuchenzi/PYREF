import json
import geopandas
json_alpha = '{"name":"chenzi","age":18}'
login_name_password = json.loads(json_alpha)
login_name_password['name'] = 'muyu'
json_beta = json.dumps(login_name_password)
assert json_alpha == json_beta

json_gamma = '[ {"name":"chenzi","age":18}, {"name":"muyu","age":28}]'
login_json_array = json.loads(json_gamma)
json_delta = json.dumps(login_json_array)
