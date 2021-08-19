from collections import defaultdict
str = "timetopractice"
pat = "toc"
len1 = len(str)
len2 = len(pat)
chars = 256
count = 0
start = 0
min_len = 256
hash_pat = [0]*chars
hash_str = [0]*chars

for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1

for j in range(0,len1):
    hash_str[ord(str[j])] += 1

    if hash_str[ord(str[j])] <= hash_pat[ord(str[j])]:
        count+=1

    if count == len2:
        while hash_str[ord(str[start])] > hash_pat[ord(str[start])] :
            if hash_str[ord(str[start])] > hash_pat[ord(str[start])]:
                  hash_str[ord(str[start])] -= 1
            start += 1
        len_window = j - start + 1
        if min_len > len_window:

            min_len = len_window
            start_index = start
print(str[start_index: start_index + min_len])