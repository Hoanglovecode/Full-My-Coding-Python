from math import*
m, n, k = map(int, input().split())
ans = 1
while (n > 0):
    if (n % 2 != 0):
        ans = ans * m % k
    m = m * m % k
    n //= 2
print(ans)
