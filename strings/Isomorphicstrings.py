str1 = 'aab'
str2 = 'xxy'
i,j=0,0
str =''
while i < len(str1) and j <len(str2):
    str1 = str1.replace(str1[i],str2[j])
    i+=1
    j+=1
print(str1)
if str1 == str2:
    print("True")