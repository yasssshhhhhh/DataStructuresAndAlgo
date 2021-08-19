nums = [1,15,10,15]
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        nums[i] = nums[i+1] - 1
print(nums)
