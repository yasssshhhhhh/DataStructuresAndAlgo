nums = [121,111,1331,1441]
print(nums)
def PalindromeArray(nums):
    for value in nums:
        ans = 0
        temp = value
        while temp>0:
            r = temp%10
            temp//=10
            ans = (ans*10) + r 
        if ans!= value:
            return 0
    return 1
print(PalindromeArray)

PalindromeArray(nums)