"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""
# First solution
a=int(input("enter a number:"))
print("The unit digt is:",a%10)
# Second solution
s=input("enter a number:")
print("The unit digt is:",s[-1])


