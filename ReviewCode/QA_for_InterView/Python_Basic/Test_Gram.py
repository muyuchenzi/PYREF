import json
import os


def read_jsonfile():
    try:
        with open(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Basic\data\them.json', 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print('文件没有被发现')
    except IOError:
        print('文件打开失败')
    return json_data


def write_jsonfile(json_data):
    if os.path.exists(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Basic\data\them_res.json'):
        os.remove(
            r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Basic\data\them_res.json')
    else:
        try:
            with open(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Basic\data\them_res.json', 'w') as f:
                json.dump(json_data, f)
        except IOError:
            print('文件写入失败')


if __name__ == "__main__":
    json_file = read_jsonfile()
    write_jsonfile(json_data=json_file)
