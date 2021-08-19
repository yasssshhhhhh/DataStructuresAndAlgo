nums = [1,3,5,7,9,11]
key = 13
mid = 0
pos = -1
def binarySearch(nums,key):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == key:
            return key

        elif key > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binarySearch(nums,key))