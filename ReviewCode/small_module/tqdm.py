from tqdm import tqdm, trange
import time
import pandas as pd


def tqdm_basic():
    for i in tqdm(range(10), desc="这是一个进度条"):
        time.sleep(0.2)
    '''
    def __init__(self, iterable=None, desc=None, total=None, leave=False,
               file=sys.stderr, ncols=None, mininterval=0.1,
               maxinterval=10.0, miniters=None, ascii=None,
               disable=False, unit='it', unit_scale=False,
               dynamic_ncols=False, smoothing=0.3, nested=False,
               bar_format=None, initial=0, gui=False):
               '''

    # iterable: 可迭代的对象, 在手动更新时不需要进行设置
    # desc: 字符串, 左边进度条描述文字
    # total: 总的项目数
    # leave: bool值, 迭代完成后是否保留进度条
    # file: 输出指向位置, 默认是终端, 一般不需要设置
    # ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
    # unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
    # unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s
    # # tqdm_basic()


def pandas_tqdm():
    df = pd.read_csv(r'E:\李震祥\PYGIT\PYref\ReviewCode\small_module\data\data_temp.csv',
                     encoding='utf-8')

    def generate_descriptive_statement(year, name, gender, count):
        year, count = str(year), str(count)
        gender = '女性' if gender == 'F' else '男性'

        return '在{}年，叫做{}性别为{}的新生儿有{}个。'.format(year, name, gender, count)

    dict_temp = {"F": '女性', "M": "男性"}
    tqdm.pandas(desc="进度")
    df.progress_apply(lambda x: dict_temp.get(x['gender']), axis=1)


def tqdm_for():
    bar = tqdm([_ for _ in "abcdefg"])
    for i in bar:
        time.sleep(0.3)
        bar.set_description(f"{i}轮")


if __name__ == '__main__':
    tqdm_basic()
