s = "yash"
def function(s):
    return s[::-1]

print(function(s))


A = ["y","a","s","h"]
start = 0
end = len(A)-1

def reverseList(A,start ,end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A
print(reverseList(A,start,end))