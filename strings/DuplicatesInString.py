s = "yaasssh"
dict1 = {} 
count = 0
for char in s:
    if char in dict1:
        dict1[char]+=1
        count+=1
    else:
        dict1[char] = 1

for k,v in dict1.items():
    if v > 1:
        print(f"{k} is {v}")

print(count)
print(dict1)
