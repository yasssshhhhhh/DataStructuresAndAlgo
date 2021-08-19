
nums = [9,4,7,6,3,1,5]
l = 0
r = len(nums)-1
def mergeSort(nums,l,r):
    if l<r:
        mid = (l+r)//2
        print(nums)
        mergeSort(nums,l,mid)
        print(nums)
        mergeSort(nums,mid+1,r)
        print(nums)
        merge(nums,l,mid,r)
        print(nums)
def merge(nums,l,mid,r):
    i = l
    j = mid+1
    b = [0]*len(nums)
    k = l
    while i<=mid and j<=r:
        if nums[i]<nums[j]:
            b[k] = nums[i]
            i+=1
        else:
            b[k] = nums[j]
            j+=1
        k+=1
    if (i>=mid):
        while j<=r:
            b[k] = nums[j]
            j+=1
            k+=1
    else:
        while i<=mid:
            b[k]=nums[i]
            i+=1
            k+=1
    # for k in range(l,len(b)):
    #     nums[k] = b[k]
    print(nums[k])

mergeSort(nums,l,r)

# arr = [9,4,7,6,3,1,5]
# def mergeSort(arr):
#     if len(arr) > 1:
 
#          # Finding the mid of the array
#         mid = len(arr)//2
 
#         # Dividing the array elements
#         L = arr[:mid]
 
#         # into 2 halves
#         R = arr[mid:]
 
#         # Sorting the first half
#         mergeSort(L)
 
#         # Sorting the second half
#         mergeSort(R)
 
#         i = j = k = 0
 
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#                 # count += len(L)
#             k += 1
 
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
 
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# # def printList(arr):
# #     for i in range(len(arr)):
# #         print(arr[i], end=" ")
# #     print()

# mergeSort(arr)
# # printList(arr)
# print(arr)
# print(count)




def merge(lefthalf, righthalf):
    i=j=0
    sorted_list = []
    
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            sorted_list.append(lefthalf[i])
            i=i+1
        else:
            sorted_list.append(righthalf[j])
            j=j+1
        k=k+1

    while i < len(lefthalf):
        sorted_list.append(lefthalf[i])
        i=i+1
        k=k+1

    while j < len(righthalf):
        sorted_list.append(righthalf[j])
        j=j+1
        k=k+1
    
    print('sorted list {}'.format(sorted_list))
    return sorted_list


def mergeSort(nlist):
    if len(nlist) <= 1:
        return nlist

    elif len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        print('splitting {}, left: {}, right: {}'.format(nlist, lefthalf, righthalf))

        # print("left_before sort ",lefthalf)
        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)
        # print("left_after sort ",lefthalf)
        return merge(lefthalf, righthalf)




nlist = [9,8,7,6,5,4,3,2]
mergeSort(nlist)
print(nlist)