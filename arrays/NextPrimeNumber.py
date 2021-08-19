a = int(input("enter number"))
k = a+1
while k:
    for i in range(2,k+1):
        if k%i == 0:
            break

    if i ==k:
        print(k)
        break
    else:
        k+=1