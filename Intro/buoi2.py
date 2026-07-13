a=int(input("Enter the month:"))
match a:
    case 1:
        print("January")
    case 2:
        print("Feburary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid day")
# Toán tử 3 ngôi
b=int(input("Nhập 1 số nguyên bất kì:"))
c="Đây là số chẵn" if b%2==0 else "Đây là số lẻ"
print(c)    