nums = [-12,11,-13,-5,6,-7,5,-3,-6]
Neg = 0
pos = len(nums)-1
curr = 0
        
while curr<=pos:
    if nums[curr] < 0:
        nums[Neg],nums[curr] = nums[curr],nums[Neg]
        curr+=1
        Neg+=1
            
    elif nums[curr] > 0:
        nums[pos],nums[curr] = nums[curr],nums[pos]
        pos = pos-1
  

print(nums)