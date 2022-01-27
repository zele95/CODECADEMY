def getX(x, nums):
    # gets the x'th integer in the sorted nums
    if x > len(nums) or nums == []:
        return 0
    else:
        sort_nums = []
        while nums != []:
            sort_nums.append(min(nums))
            nums.remove(min(nums))
        return sort_nums[x-1]


print(getX(2, [6, 3, -1, 5]))
