
def SearchMatrix():
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 60
    row = len(matrix)
    col = len(matrix[0])
    # for i in range(row):
    #     for j in range(col):
    #         if matrix[i][j] == target:
    #             return True
    # return False

    for i in range(row):
        if max(matrix[i]) < target:
            continue
        else:
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
    return False 
print(SearchMatrix())