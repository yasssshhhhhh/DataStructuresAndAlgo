grid = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]]
top = 0
bottom =len(grid)-1 
left = 0
right = len(grid[0])-1
dir = 0
while top<=bottom and left<= right:
    if dir == 0:
        for i in range(left,right+1):
            print(grid[top][i],end = " ")
        top+=1
    elif dir ==1:
        for i in range(top,bottom+1):
            print(grid[i][right],end = " ")
        right-=1
    elif dir == 2:
        for i in range(right,left-1,-1):
            print(grid[bottom][i],end=" ")
        bottom-=1
    elif dir == 3:
        for i in range(bottom,top-1,-1):
            print(grid[i][left],end=" ")
        left+=1
    dir=(dir+1)%4
