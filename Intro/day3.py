#input trả về  kiểu str vì vậy phải ép kiểu dữ liệu
a=float(input('Xin mời nhập bán kính R:'))
b=3.14*a*a
c=2*3.14*a
print('Diện tích hình tròn là:','{:.2f}'.format(b))
print('Chu vi hình tròn là:','{:.2f}'.format(c))
a=int(input('Nhập chiều dài:'))
b=int(input('Nhập chiều rộng:'))
chuvi=2*(a+b)
dientich=a*b
print('Chu vi=',chuvi,' Diện tích=',dientich)
#Nhập 2 3 4 số trên cùng 1 dòng 
a,b,c,d=map(int,input().split())
print(a+b+c+d)
x,y,z,t=map(float,input('Tích 4 số nhập từ bàn phím:').split())
print(int(x*y*z*t))
