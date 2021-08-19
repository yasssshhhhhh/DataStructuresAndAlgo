nums = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
dict1={}
for i in range(len(nums)):
    if nums[i] not in dict1:
        dict1[nums[i]] = 1
    else:
        dict1[nums[i]]+=1
first_max = -10**8
sec_max = -10**8
 
for it in dict1:
    if (dict1[it] > first_max):
        sec_max = first_max
        first_max = dict1[it]
             
    elif (dict1[it] > sec_max):
        sec_max = dict1[it]
for it in dict1:
    if (dict1[it] == sec_max):
        print(it)
print(sec_max)
print(dict1)