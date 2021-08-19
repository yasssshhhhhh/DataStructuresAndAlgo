from collections import defaultdict

nums = [1,5,7,1]
k = 6
dict1 = defaultdict(int)
# count = 0
# for value in nums:                               
# #  if dict1[value] > 0:
#     count += dict1[value]
#     dict1[k-value] += 1
    
# print(count)

count = 0
for value in nums:
    if k-value not in dict1:
        dict1[value]+=1
        print(dict1)
    else:
        count+= dict1[k-value]
        dict1[value]+=1
print(count)


























# count = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == k:
#             count+=1
# print(count)