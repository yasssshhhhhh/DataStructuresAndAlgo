s = "AACECAAAA"
start = 0
end = len(s)-1
stripped = ""
def IsPalindrome(start,end,s):
    global broke
    while start <= end:
        if s[start] != s[end]:
            broke = end
            return False
        start+=1
        end-=1
    return True

# print(IsPalindrome(start,end,s))
while not IsPalindrome(start,end,s):
    # if not IsPalindrome(start,end,s):
        stripped += s[-1]
        s=s[:len(s)-1]
        end = len(s)-1
print(len(stripped))

print(s[-1])

