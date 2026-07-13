#Cấu trúc rẽ nhánh if else
#if(condition):
#    <code>
a=float(input('Nhập vào điểm lí:'))
if a>=9.25 and a<=10:print('Bạn có kiến thức tốt')#Cách viết cùng 1 dòng
elif (a>=8) and (a<=9):
    print('Bạn đã nắm được kiến thức')
else:
    print('Bạn vẫn còn kém ')
#Toán tử 3 ngôi
b=int(input('Nhập số nguyên bất kì:'))
temp='Đây là số chẵn' if(b%2==0) else 'Đây là số lẻ'
print(temp)
#If lồng nhau