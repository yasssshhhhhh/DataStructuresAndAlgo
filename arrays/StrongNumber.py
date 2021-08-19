value = 17
nums = [x for x in range(1,value+1)]
for i in range(len(nums)-1):
    if i == len(nums):
        i = 0
    if nums[i]%2 == 0:
        nums.pop(i)
    

