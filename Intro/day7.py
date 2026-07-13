#Vòng while
n=1
while n<=5:
    print('Vòng while thứ ',n)
    n+=1
else:
    print('Vòng while kết thúc khi n=',n)
#Yêu cầu người dùng nhập số dương,sai thì bắt nhập lại
while True:#Vòng lặp vĩnh viễn(luôn cần break để dừng)
    a=float(input('Mời nhập số dương:'))
    if a>0:
        print('OK')
        break