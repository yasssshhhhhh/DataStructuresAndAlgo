def Quicksort(arr,left,right):
    if left < right:
        pivot = partion(arr,left,right)
        Quicksort(arr,left,pivot-1)
        Quicksort(arr,pivot+1,right)


def partion(arr,left,right):
    i = left
    j = right
    pivot = arr[left]
    while i<j:
        while i < right and arr[i] <= pivot:
            i+=1
        while j > left and arr[j] > pivot:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[j],arr[left] = arr[left],arr[j]
    return j

arr=[10, 7, 8, 9, 1, 5]
Quicksort(arr,0,len(arr)-1)
print(arr)



