#Vòng lặp for và hàm range()
   #range(start,stop,step)
   #start:bắt đầu mặc định là 0
   #stop:số kết thúc và k được lấy số này
   #step:Bước nhảy mặc định là 1
#Ví dụ range(5)==range(0,5,1):bắt đầu 0 đến 4 bước là 1
##In ra chuỗi các số chẵn từ 1 đến 100
for i in range(2,101,2):
    print(i,end=' ')#Không dùng end thì nó sẽ xuống dòng
print(' ')
for i in range(5):
    print('Đây là số ',i)
#Tính tổng bình phương từ 1 đến 100
n=100
s=0
for i in range(n+1):
   s+=pow(i,2)
print('Tổng bình phương từ 1 đến 100=',s)
#Ước của 100
print('Ước của 100 là:')
for i in range(1,101):
    if(n%i==0):
     print(i,end=' ')
print(' ')#cout<<endl trong C++
#Dòng i+=1 không bị ảnh hưởng trong vòng for
for i in range(1,7,2):
   print(i)
   i+=4
   print(i)
#Break(dừng) and continue
                #Liệt kê các số đến số chia hết cho 7 thì dừng
for i in range(1,10):
    print(i,end=' ')
    if i%7==0:
       break
    print('Số này không chia hết cho 7')
print('Dừng')
                #Nhập đúng số 2025 thì dừng
a=float(input('Mời nhập đúng số 2025:'))
for i in range(pow(10,10)):
    if(a==2025):
        print('OK')
        break
    else:
        a=float(input('Mời nhập lại:'))
#Nexted loop:Vòng for lồng nhau
for i in range(2):
    for j in range(4):
       print(i,j)


