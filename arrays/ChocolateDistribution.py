m = 3
nums = [7, 3, 2, 4, 9, 12, 56]
# nums = [3, 4, 1, 9, 56, 7, 9, 12]
nums.sort()
start = 0
min_value = 1000
for i in range(len(nums)):
    if i >= m-1:
        difference = nums[i] - nums[start]
        min_value = min(min_value,difference)
        start +=1
print(min_value)        
   