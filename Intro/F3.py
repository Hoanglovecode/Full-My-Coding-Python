# Cách 1
a=int(input())
print(bin(a)[2:])
# Cách 2
n=int(input())
if n>=0 and n<=100000:
    if(n==0):print(0)
    else:
        s=""
        while(n>0):
            s=str(n%2)+s
            n//=2
        print(s)
#Chuyển đổi hệ nhị sang thập
x=input("Chuyển hệ nhị sang thập:")
num=len(x)
sum=0
# dùng hàm enumerate khi cần in index vừa in giá trị
for index,i in enumerate(x):
    sum+=int(i)*2**(num-1-index)
print(sum)
