nums = [1,2,3,4,2]
dict = {}
for value in nums:
    if value in dict:
        print(value)
    else:
        dict[value] = 1