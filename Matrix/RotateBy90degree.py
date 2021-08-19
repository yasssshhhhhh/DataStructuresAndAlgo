mat = [[1 ,2, 3], 
       [4 ,5 ,6],
       [7, 8, 9]]
row = len(mat)
col = len(mat[0])
for j in range(col):
    for i in range(row-1,-1,-1):
        print(mat[i][j]) 