nums = [4,2,-3,1,6]
sum = 0
s = set()
for i in range(len(nums)):
    sum += nums[i]
 
    if sum == 0 or sum in s:
        print(True)
    s.add(sum)
 
print(False)