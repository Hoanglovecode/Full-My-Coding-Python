n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    for j in range(n-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
for i in range(n):
    print(a[i],end=" ")