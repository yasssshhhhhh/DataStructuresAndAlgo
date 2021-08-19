grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
r = len(grid)
c = len(grid[0])
perimeter = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 1:
            perimeter+=4
            if i>0 and grid[i-1][j] ==1:
                perimeter-=2
            if j>0 and grid[i][j-1]==1:
                perimeter-=2
print(perimeter)