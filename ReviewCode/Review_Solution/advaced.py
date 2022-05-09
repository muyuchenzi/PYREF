# python的高级用法。
import json

json_str = '{"name":"qiye","age":15}'

stu = json.loads(json_str)
print(type(stu))

