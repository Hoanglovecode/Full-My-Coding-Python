from math import*
n,m=map(int,input().split())
if (n >= 1 and m >= 1 and m <= pow(10, 9) and n <= pow(10, 9)):
    if (n == 1 or n == 2):print("1")
    else:
        a =(pow(((1 + sqrt(5)) / 2), n) - pow(((1 - sqrt(5)) / 2), n)) / sqrt(5)
        b=a%m
        print(int(b))