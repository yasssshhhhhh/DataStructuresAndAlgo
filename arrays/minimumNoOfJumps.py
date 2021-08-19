# Naive Appraoch [ doesn't work when there are zeroes ]

# count = 0
# i = 0


# while i < len(nums):
#     i = i + nums[i]
#     count+=1
#     if i >= len(nums)-1:
#         break
# print(count)
# def MinJumps():
#     nums =[1, 1, 3, 2, 6, 7]
#     count = 0
#     reachable = 0
#     for i in range(len(nums)):
#         if reachable < i :
#             return False
#         reachable = max(reachable,i+nums[i])
#     return True

# print(MinJumps())
nums = [0, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
def MinJumps(nums):
    reachable = nums[0]
    n = len(nums)-1
    step = nums[0]
    Jumps = 1
    if n == 1:
        return 0
    elif nums[0] == 0:
        return -1
    else:
        for i in range(1,len(nums)-1):
            if i == n-1:
                return Jumps
            reachable = max(reachable,i+nums[i])
            step-=1
            if step == 0:
                Jumps+=1
                if i >= reachable:
                    return -1
                step = reachable-i
print(MinJumps(nums))


