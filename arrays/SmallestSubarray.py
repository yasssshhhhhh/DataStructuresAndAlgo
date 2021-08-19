import sys
class Solution:
    def sb(self, a, n, x):
        # Your code goes here
        cur_sum = 0
        start = 0
        length = 0
        min_len = sys.maxsize
        for i in range(len(a)):
            cur_sum += a[i]
            while cur_sum > x:
                length = (i - start) + 1
                cur_sum -= a[start]
                start += 1
                min_len = min(min_len, length)
        return min_len