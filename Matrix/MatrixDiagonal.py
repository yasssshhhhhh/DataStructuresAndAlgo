# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]

mat =  [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
sum = 0
n = len(mat)
for i in range(n):
    sum+=mat[i][i] + mat[i][n-i-1]
if n%2 ==1:
    sum-=mat[n//2][n//2]
print(sum)


