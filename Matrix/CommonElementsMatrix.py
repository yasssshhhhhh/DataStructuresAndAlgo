mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

dict1 = {}
row = len(mat)
col = len(mat[0])


for j in range(col):
    dict1[mat[0][j]] = 1
for i in range(1,row):
    for j in range(col):
         if (mat[i][j] in dict1.keys() and dict1[mat[i][j]] == i):
                                  
            # we increment count of the
            # element in map by 1
                dict1[mat[i][j]] = i + 1
 
                # If this is last row
                if i == row - 1:
                    print(mat[i][j], end = " ")
# print(dict1)

            