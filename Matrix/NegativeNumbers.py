nums = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

count = 0
n = len(nums)
for array in nums:
    for j in range(len(array)):
        if array[j] < 0:
            count+=1
print(count)