n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]

dict_sum = {i:[0, 0] for i in range(6)}

for d in dice:
    d[1], d[2] = d[2], d[1]
    for i in range(3):
        a, b = d[i], d[5-i]
        dict_sum[i][1], dict_sum[5-i][1] = b, a

        d[i] = d[5-i] = 0
        num = max(d)
        dict_sum[i][0] += num
        dict_sum[5-i][0] += num
        d[i], d[5-i] = a, b


print(max([dict_sum[i][0] for i in range(6)]))