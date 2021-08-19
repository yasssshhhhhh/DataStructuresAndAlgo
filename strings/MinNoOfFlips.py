s = "111000"
  #  1010101010
  #  0101010101
counter1 = 0
counter2 = 0
for i in range(len(s)):
    if i&1 and s[i] == '0':
        counter1+=1
    if i%2==0 and s[i] =='1':
        counter1+=1
    if i&1 and s[i] == '1':
        counter2+=1
    if i%2==0 and s[i] =='0':
        counter2+=1
count = min(counter1,counter2)
print(count)