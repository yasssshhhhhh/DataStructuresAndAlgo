nums = [1,2,3,4]
k = 1
# for i in range(k+1):
#     temp = nums[0]
            
# for j in range(len(nums)-1):
#     nums[j] = nums[j+1]
# nums[len(nums)-1] = temp

# for i in range(k):
#     temp = nums[-1]  
#     for j in range(len(nums)-1,-1,-1):
#         print(len(nums)-1)
#         nums[j] = nums[j-1]
#     nums[0] = temp
# print(nums)

k%=len(nums)
nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
print(nums)





#         for i in nums[0:k+1]:
#             a = nums.pop(0)
#             nums.append(a)
#         j = len(nums)-1
#         for i in range(k+1):
#             temp = nums[-1]
            
#             for j in range(-1,len(nums)-1):
#                 nums[j] = nums[j-1]
#             nums[0] = temp