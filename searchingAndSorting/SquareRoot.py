import math

x =  3
count = 0
for i in range(1,x):
    if math.sqrt(i)%1==0:
        count+=1

print(count)

