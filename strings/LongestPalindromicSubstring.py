


# def IsPalindrome(start,end,s):
#     while start <= end:
#         if s[start] != s[end]:
#             return False
#         start+=1
#         end-=1
#     return True


# def LongestPalindrome():

#     s = "aaaabbaa"
#     maxcount = 0
#     result = ""

#     if len(s)==1:
#         return s
    
#     for i in range(len(s)):
#         test = ""
#         test+= s[i]
#         for j in range(i+1,len(s)):
#             test += s[j]
#             if IsPalindrome(0,len(test)-1,test):
#                 count = len(test)
#                 if count > maxcount:
#                     maxcount = count
#                     result = test
#     if maxcount == 0:
#         result = s[0]
#     return result

            
#             # print(test)
# print(LongestPalindrome())


def palindrome():
    s = "babad"
    n = len(s)
    if len(s) == 1:
        return s
    max_len = 1
    st,end = 0,0
        

    for i in range(n-1):
        l,r = i,i
        while l>=0 and r<n:
            if s[l] == s[r]:
                l = l-1
                r = r+1
            else:
                break
        length = r-l-1
        if length > max_len:
            max_len = length
            st, end = l+1,r-1
    return s[st:end+1]
print(palindrome())