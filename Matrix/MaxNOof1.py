matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]
row = len(matrix)
col = len(matrix[0])
max_Count = 0
row = -1
for i in range(row):
    count  = 0
    for j in range(col):
        if matrix[i][j] == 1:
            count+=1
        if count > max_Count
        max_Count = count
        row = i


# 2ND APPROACH
max_count = 0
        row = -1
    	for i in range(n):
            count = 0
            j = 0
            if arr[i][j] == 1:
                count += m
                if count > max_count:
                    max_count = count
                    row = i
            else:
                while arr[i][j] == 0:
                    j += 1
                    if j >= m:
                        break
                count += (m - j)
                if count > max_count:
                    max_count = count
                    row = i