nums = [2, 7, 9, 5, 8, 7, 4]
start = 0
i = 0
k = 6
while i <= len(nums)-1:
    if nums[i] <= k:
        nums[i],nums[start] = nums[start],nums[i]
        i+=1
        start+=1
    else:
        i+=1
print(nums)
