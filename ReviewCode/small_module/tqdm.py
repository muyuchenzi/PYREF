from tqdm import tqdm, trange
import time


def tqdm_basic():
    for i in tqdm(range(10), desc="这是一个进度条"):
        time.sleep(0.2)


tqdm_basic()

bar = tqdm(range(10))
for i in bar:
    time.sleep(0.2)
    bar.set_description(f"{i}轮")
