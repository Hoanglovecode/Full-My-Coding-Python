from math import*
a=int(input())
if a>=2 and a<=1000:
    for i in range(2,a+1):
        isprime=True
        for j in range (2,int(sqrt(i))+1):
            if i%j==0:
                isprime=False
                break
        if isprime==True and a%i==0:
                print(i,end=" ")