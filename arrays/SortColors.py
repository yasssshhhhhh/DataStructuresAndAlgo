nums = [2,0,2,1,1,0]
L = 0
R = len(nums)-1
curr = 0
        
while curr<=R:
    if nums[curr] == 0:
        nums[L],nums[curr] = nums[curr],nums[L]
        curr = curr + 1
        L = L + 1
    elif nums[curr] == 1:
        curr = curr + 1
    else:
        nums[R],nums[curr] = nums[curr],nums[R]
        R= R-1

print(nums)
