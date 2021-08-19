s = ['act','god','cat','dog','tac']
dict1 = {}
j = 0
value = 0
for i in s:
    for j in i:
        value+=ord(j)
    dict1[i] = value
    value = 0
print(dict1)
# s = 'ACT'
# print(ord(s[0]))