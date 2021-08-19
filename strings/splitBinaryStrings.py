s = "0100110101"
count = 0
count1 = 0
count0 = 0
for i in range(len(s)):
    if s[i] == '0':
        count0 +=1
    else:
        count1+=1

    if count0 == count1:
        count+=1
print(count)