# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
def solution(nums, target):
    for i, num in enumerate(nums):
        if target - num in nums[i:]:
            return [i, nums.index(target - num)]
        else:
            return []


def answer(nums, target):
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0

    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        x = nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum_val = x + nums[j] + nums[k]
            if sum_val == target:
                ans.append((i, j, k))
                j += 1
                k -= 1
                while nums[j] == nums[j + 1]:
                    j += 1
                while nums[k] == nums[k - 1]:
                    k -= 1
            elif sum_val > target:
                k -= 1
            elif sum_val < target:
                j += 1
    return ans


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = solution(nums, target)
    ans = answer(nums, target)
