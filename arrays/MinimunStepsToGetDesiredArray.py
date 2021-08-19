nums = [16,16,16]
count_s = 0
div = 0
maxdiv = 0
i = len(nums)-1
while(i!=-1):
    if nums[i]%2 == 0:
        nums[i]//=2
        div = div + 1
    else:
        nums[i]-= 1
        count_s+=1
    maxdiv = max(div,maxdiv)
    if nums[i] == 0:
        div = 0
        i-=1
sums = count_s + maxdiv
print(sums)
print(nums)
