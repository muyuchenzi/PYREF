from collections import defaultdict


def solution():
    array = [[0 for _ in range(4)] for _ in range(10)]
    array[1][0] = 1
    array[0][1] = 5


if __name__ == "__main__":
    solution()
