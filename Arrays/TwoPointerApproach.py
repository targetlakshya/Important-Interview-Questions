'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.'''


def threeSum(nums):
    nums.sort()
    print(nums)
    result = []
    for i in range(len(nums)):
        print(f"i = {i}")
        if i > 0 and nums[i] == nums[i-1]:
            continue
        print(f"nums[i] = {nums[i]}")
        left = i+1
        print(f"left = {left}")
        right = len(nums)-1
        print(f"right = {right}")
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            print(f"total = {total}")
            if total < 0:
                left += 1
                print(f"left = {left}")
            elif total > 0:
                right -= 1
                print(f"right = {right}")
            else:
                result.append([nums[i], nums[left], nums[right]])
                print(f"result = {result}")
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                    print(f"left after while = {left}")
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                    print(f"right after while = {right}")
                left += 1
                print(f"left after while = {left}")
                right -= 1
                print(f"right after while = {right}")
    return result

nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(result)
