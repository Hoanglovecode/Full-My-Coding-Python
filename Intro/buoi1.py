from math import*
r=float(input('Nhập vào bán kính R:'))
dientich=pi*r*r
print('Diện tích hình tròn=','{:.2f}'.format(dientich))
hours=int(input("Nhập vào số giờ:"))
print("Số phút và giây tương ứng là:",hours*60,hours*3600,sep=" và ")
a=int(input("Nhập vào số nguyên n:"))
print("Tổng số đo các góc đa giác đều",a,"cạnh là:",(a-2)*180)
# Bài tập hoán đổi vị trí 2 số a và b
x,y=map(int,input("Nhập 2 số nguyên trên cùng 1 dòng:").split())
# Cách 1
temp=x
x=y
y=temp
# Cách 2
x,y=y,x
print("Giá trị lúc sau là:",x,y,sep=" ")
