dict1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
sum = 0
s = "MCMIV"
length = len(s)
for i in range(length-1):
    if dict1[s[i]] < dict1[s[i+1]]:
        sum += dict1[s[i+1]] - dict1[s[i]]
        # i+=1
        # continue
    sum += dict1[s[i]]
print(sum)

