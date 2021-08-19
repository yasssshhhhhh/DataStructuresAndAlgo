mat=[[10,20,30,40],
    [15,25,35,45], 
    [27,29,37,48], 
    [32,33,39,50]]
# mat = [[1,5,3],[2,8,7]]
n = len(mat)
temp = [0] * (n * n)
k = 0
col = len(mat)
for i in range(0, n) :
        
    for j in range(0, n) :
            
        temp[k] = mat[i][j]
        k += 1
temp.sort()
k = 0
for i in range(0, n) :    
    for j in range(0, n) :
        mat[i][j] = temp[k]
        k += 1


print(mat)