
A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]

i=0
j=0
k=0
while i < len(A) and j < len(B) and k < len(C):
    if A[i] == B[j] and B[j]==C[k]:
        print(A[i])
        i+=1
        j+=1
        k+=1
    elif A[i] > B[j]:
        j+=1
    elif B[i] > C[j]:
        k+=1
    else:
        i+=1
    






























# dictt = {}
# for value in A:
#     if value in dictt:
#         pass
#     else:
#         dictt[value] = 1

# for value in B:
#     if value in dictt:
#         dictt[value]+=1
#     else:
#         pass

# for value in C:
#     if value in dictt:
#         dictt[value]+=1
#     else:
#         pass
# for i in dictt:
#     if dictt[i] > 2:
#         print(i)
        
