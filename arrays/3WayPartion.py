nums = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
a = 14
b = 20
start = 0
end = len(nums)-1
i = 0
while i<=end:
    if nums[i] < a:
        nums[i],nums[start] = nums[start],nums[i]
        start+=1
        i+=1
    elif nums[i] > b:
        nums[i],nums[end] = nums[end],nums[i]
        end-=1
    else:
        i+=1
print(nums)
