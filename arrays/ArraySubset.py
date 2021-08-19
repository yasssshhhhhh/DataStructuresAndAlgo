a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]
# dict1 = {}
# for value in a1:   
#     if value not in dict1:
#         dict1[value] = 1



def isSubset( a1, a2):
    for value in a2:
        if value not in a1:
            return "No"
    return "Yes"


print(isSubset(a1,a2))