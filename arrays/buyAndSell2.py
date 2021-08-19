nums = [5,2,6,1,4,7,3,6]
profit = 0
i=0
for i in range(i+1,len(nums)):
    if nums[i] > nums[i-1]:
        profit+=nums[i]-nums[i-1]
print(profit)