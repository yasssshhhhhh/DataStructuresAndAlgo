def longestSubarray():
    # arr = [8,8,9,9,3,4]
    # arr = [20,10,23,22,21]
    # arr = [2,6,1,9,4,5,3]
    arr = [1,2,3,4,5]
    # arr = [1,2,3,4,5,7,8,9]
    dict1 = {}
    count = 0
    min_value = min(arr)-1
    max_value = max(arr)
    current_val = min_value
    max_count = 0
    for value in arr:
        if value not in dict1:
            dict1[value] = 1


    for value in range(min_value, max_value):
        if current_val + 1 in dict1:
            count += 1
            current_val += 1
        else:
            max_count = max(count, max_count)
            current_val += 1
            count = 0
    max_count = max(count,max_count)
    print(max_count)

longestSubarray()