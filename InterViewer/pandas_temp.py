import pandas as pd
from string import ascii_lowercase


def solution():
    nums = [2, 2, 7, 7, 11, 15, -2]
    target = 9
    nums.sort()
    result = []
    left, right = 0, len(nums) - 1
    while left < right:
        sum_nums = nums[left] + nums[right]
        if sum_nums < target:
            left += 1
        elif sum_nums > target:
            right -= 1
        else:
            result.append((nums[left], nums[right]))
            left += 1
            right -= 1
