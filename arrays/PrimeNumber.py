def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            break

    else:
        print(num,end=" ")


a = int(input("enter lower bound:"))
b = int(input("enter upper bound"))
for i in range(a,b+1):
    if i!=1:
        isPrime(i)