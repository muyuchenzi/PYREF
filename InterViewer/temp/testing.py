def solution():
    nums = [0, 0, 0]
    nums.sort()
    result = []
    for i in range(len(nums)):
        x = nums[i]
        if x > 0:
            break
        left = i + 1
        right = len(nums) - 1
        # TODO 这里需要注意，如果起点与后一个相同的话，跳过
        if nums[i] == nums[i - 1]:
            continue
        while left < right:
            sum_val = x + nums[left] + nums[right]
            if sum_val > 0:
                right -= 1
            elif sum_val < 0:
                left += 1
            else:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1


if __name__ == "__main__":
    solution()
