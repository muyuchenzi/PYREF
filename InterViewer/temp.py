# def solution():
#     nums = [2, 3, 1, 2, 4, 3]
#     target = 7
#
#     total = 0
#     left = 0
#     res = float("inf")
#     res > 10
#     for right in range(len(nums)):
#         total += nums[right]
#         while total >= target:
#             res = min(res, right - left + 1)
#             total -= nums[left]
#             left += 1
#
from itertools import permutations, combinations


def solution():
    cards = [3, 4, 2, 3, 4, 7]

    res = float("inf")
    left, right = 0, 0
    window = set()
    while right < len(cards):
        current = cards[right]
        while current in window:
            res = min(right - left + 1, res)
            d = cards[left]
            window.remove(d)
            left += 1
        window.add(current)
        right += 1
    return -1 if res == float("inf") else res


test = [1, 2, 3]
test.remove(1)

if __name__ == '__main__':
    fin_res = solution()
