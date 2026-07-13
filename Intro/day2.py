#Bài:5(28tech)
#Toán tử gán
# x**=2 (x mũ 2)
a,b,c=100,200,300
d,e='hello',1
print(a,b,c)
a,b,c=c,b,a
print(a,b,c)
print(d,e)
#Toán tử toán học
#chia lấy nguyên //
# chia lấy dư %
print(a//b)#a=300 b=200 do line 6 đã hoán vị
#Toán tử so sánh
# != :so sánh khác
# ==: so sán bằng
print(100!=200)
# Toán tử logic
x=200
# and or not
print(not(x<100))#true
print((x>100) and (x<300))#True
#Toán tử nhận dạng 
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is not b)
print(a is b)
#Toán tử thành viên
s='lê văn hoàng 25dt2'
print('25dt2' in s)#true
print('123' not in s)#true
#BT
r=5.75
chuvi=2*3.14*r
dientich=3.14*r*r
print('Chu vi hình tròn bán kính=5.75 là:','{:.2f}'.format(chuvi))
print('Diện tích hình tròn bánh kính=5.75 là:','%.2f'%(dientich))