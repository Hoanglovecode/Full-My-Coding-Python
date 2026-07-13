#Bài:1->4(28tech)
#Đây là chú thích
""""
Đặt tên biến không được có dấu cách,kí tự special,bắt đầu bằng con số,..
"""
print('lê văn hoàng')
print('lê','văn','hoàng',sep=' ')#sep là phân cách
print('lê','văn','hoàng',sep=' ',end='!\n')#end là kí tự cần kết thúc
print('sep là dấu phân cách,end là kí tự kết thúc')
a=100
b=2.2329
c='hello' 
d=5+4j
print(a,b,c,d,sep='--')
print(type(a),type(b),type(c),type(d),sep='--')
#print('%.nf'%biến) làm tròn biết đến hàng phần n
print('%.3f'%b)#cách 1
#print('{:.nf}'.format(biến))
print('{:.3f}'.format(b))#cách 2
#ví dụ
print('{:.2f}'.format(b))
print('%.1f'%b)
#in ra phần thực và ảo
e=5+12j
print(e.real)
print(e.imag)#imaginary(adj):phần ảo,ảo,tưởng tượng
#bool:xác định True hay False
#trường hợp có kí tự Rỗng hay s ố 0 đều in ra false
#ví dụ:
f=0
g=''
print(bool(a),bool(b),bool(c),bool(d),bool(e),bool(f),bool(g))
t='234523'
j='''Hello em'''
print(j,t,sep=' ')
print(type(t),type(j),sep='---')
#Lưu ý khi ép kiểu dữ liệu
i=23.4543
print(int(i))
a1=50
print(float(a1))
o='4434234'#sâu này chỉ chứa số nếu có kí tự thì sẽ lỗi
print(float(o))
a=5.3435345
print('{:.4f}'.format(a))
print('{:.3f}'.format(a))