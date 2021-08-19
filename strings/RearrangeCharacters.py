s='aabbbbb'
dict1={}
max_value = 0
for i in range(len(s)):
    if s[i] in dict1:
        dict1[s[i]]+=1
    else:
        dict1[s[i]] =1
for key,value in dict1.items():
    if max_value < value:
        max_value = value

if max_value <= len(s)- max_value +1:
    print(1)
else:
    print(0)