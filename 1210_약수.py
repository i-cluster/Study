# JO 2809

n = int(input())
divisor = [1, n]

s, e, k = 2, n-1, 2
while s < e:
    if not n % s:
        arr = [s, n // s] if n != s ** 2 else [s]
        divisor = divisor[:k // 2] + arr + divisor[k // 2:]
        k += 2
        e = n // s
    s += 1

for d in divisor:
    print(d, end=' ')