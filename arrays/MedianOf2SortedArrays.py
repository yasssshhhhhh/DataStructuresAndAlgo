
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45,51,70]
l1 = 0
r1 = len(ar1)-1
l2 = 0
r2 = len(ar2)-1
median1 = (l1+r1)//2
median2 = (l2+r2)//2
median = (ar1[median1] + ar2[median2])//2
print(median)
