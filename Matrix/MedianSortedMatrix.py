matrix = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
row = len(matrix)
col = len(matrix[0])
array = []
for i in range(col):
    for j in range(row):
        array.append(matrix[j][i])
array.sort()
l = 0
r = len(array)
median = (l+r)//2
print(array[median])

# NOT EFFICIENT


# DO WITH BINARY SEARCH (IMP)