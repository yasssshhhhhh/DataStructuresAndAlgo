
i = 1
intervals = [[1,3],[2, 6],[8,10],[15,18]]
intervals.sort()
if len(intervals) < 2:
    print(intervals)
    
while i < len(intervals):
    if intervals[i][0] <= intervals[i-1][1]:
        intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
        intervals.pop(i)
    else: 
        i = i+1
print(intervals)