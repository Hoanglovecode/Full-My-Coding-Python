from math import*
r=float(input('Nhập vào bàn phím bán kính R đường tròn:'))
chuvi=2*pi*r
dientich=pi*r*r
print('Chu vi=','{:.3f}'.format(chuvi),'Diện tích=','{:.3f}'.format(dientich))
a,b=map(float,input('Nhập vào lần lượt chiều dài và chiều rộng của hcn:').split())
print('Chu vi và diện tích hình chữ nhật=',2*(a+b),' và ',a*b)
