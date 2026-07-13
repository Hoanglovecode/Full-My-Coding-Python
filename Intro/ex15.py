# Nhập vào số giây bất kỳ t (t là số nguyên dương bất kỳ)
#     In ra màn hình thời gian tương ứng trong ngày dưới dạng
#     hh : mm : ss
t=int(input("Enter the second:"))
h=(t//3600)%24
p=(t%3600)//60
s=t%60
print(h,":",p,":",s)