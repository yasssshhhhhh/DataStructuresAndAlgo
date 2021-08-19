# Brute-Force Approach   
nums = [-5,4,6,-3,4,-1]
# nums = [-1,-2,-3,-4]
# nums = [23,2,4,6,7]
# max_value = -10000
# i = 0
# for i in range(len(nums)):
#     runningSum = 0
#     for j in range (i,len(nums)):
#         runningSum = runningSum + nums[j]
#         max_value = max(runningSum,max_value)

# print(max_value)
# [-5,-1,5,2,6,5,4,10,7 ,11,10, 6, 3, 7, 6,-3, 1, 0, 4, 3,-1] = runningSum
# [-5,-1,5,5,6,6,6,10,10,11,11,11,11,11,11,11,11,11,11,11,11] = max_value

# [ KADENE's Algorithm]

maxsum = 0
cursum = 0
for i in range(len(nums)):
    cursum+= nums[i]
    if cursum>maxsum:
        maxsum = cursum
    if cursum < 0:
        cursum = 0
print(maxsum)

