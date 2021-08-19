nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
target = 10

i = 0
res =[]
while i < len(nums):
    if nums[i] == target:
        res.append(i)
    else:
        pass

    i+=1

if len(res) == 0:
    print(-1,-1)
else:
    print(res[0],res[len(res)-1])








































# target = 5
# start = 0
# end = 0
# def firstAndLast(start,end,x,nums):
#     for i in range(len(nums)):
#         if nums[i] == x and start == 0 and end == 0:
#                 start = i
#                 end = i
#         if nums[i] == x and end == i:
#             end = i
#     return start,end
# print(firstAndLast(start,end,x,nums))


# class solution:
#     def searchrange(self,nums,target):
#         left = self.binarySearch(nums,target,True)
#         right = self.binarySearch(nums,target,False)
#         return[left,right]
#     def binarySearch(self,nums,target,leftbias):
#         low = 0
#         high = len(nums)-1
#         i = -1
#         while low<=high:
#             mid = low + (high-low)//2
#             if target > nums[mid]:
#                 low = mid+1

#             elif target < nums[mid]:
#                 high = mid-1
#             else:
#                 i = mid
#                 if leftbias:
#                     high = mid-1
#                 else:
#                     low = mid+1

#         return i

# sol = solution()
# print(sol.searchrange(nums,target))