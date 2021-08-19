s = "abba"
start = 0
end = len(s)-1
def IsPalindrome(start,end,s):
    while start <= end:
        if s[start] != s[end]:
            return False
        start+=1
        end-=1
    return True

print(IsPalindrome(start,end,s))