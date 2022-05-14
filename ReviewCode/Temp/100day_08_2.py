from abc import ABCMeta, abstractclassmethod
from random import randint, randrange
import time


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ("_name", "_hp")

    def __init__(self, name, hp) -> None:
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractclassmethod
    def attact(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0) -> None:
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        return f"{self._hour}:{self._minute}:{self._second}"


def main():
    local_time = time.localtime()
    # year=local_time.tm_year
    # day=local_time.tm_yday
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    print(local_time)
    clock = Clock(hour, minute, second)
    count = 10
    while count:
        print(clock.show_time())
        time.sleep(1)
        clock.run()
        count -= 1


if __name__ == "__main__":
    main()
