# Brute_force
# nums = [7,1,5,3,6,4]
# differnce = 0
# max_value = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[j] - nums[i] > 0:
#             max_value = max(max_value, nums[j]-nums[i])
# print(max_value)


nums = [7,1,5,3,6,4]
minSoFar = nums[0]
maxProfit = 0 
for i in range(len(nums)):
    minSoFar = min(minSoFar,nums[i])
    profit = nums[i] - minSoFar
    maxProfit = max(profit,maxProfit)
print(maxProfit)
