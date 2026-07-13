from math import *
a = int(input())
if a > 0 and a < pow(10, 6):
 dem = 0
 d = b = a
 while (a > 0):
    a //= 10
    dem += 1
 tong = 0
 while (b > 0):
    c = b % 10
    tong += pow(c, dem)
    b //= 10
 if (tong == d):
    print("YES")
 else:
    print("NO")
