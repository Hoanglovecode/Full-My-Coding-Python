from math import*
x,n=map(float,input().split())
n=int(n)
if (abs(x)<100) and(n<20):
    s=1.0
    for i in range(1,n+1,1):
        s+=pow(x,i)/factorial(i)
    print(f"{s:.2f}")
