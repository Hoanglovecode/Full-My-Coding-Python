n = int(input())
f0, f1 = 0, 1
for i in range(0, n + 1):
    if i == 0:
        print(f0, end=" ")
    elif i == 1:
        print(f1, end=" ")
    else:
        fn = f0 + f1
        print(fn, end=" ")
        f0, f1 = f1, fn
