from math import*
a=int(input())
dem=0
for i in range(1,int(sqrt(a))+1):
    if(a%i==0):
        if(i*i==a):dem+=1
        else:dem+=2
print(dem)