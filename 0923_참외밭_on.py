# https://www.acmicpc.net/problem/2477

k = int(input())
d, l = [], []

# field = [[0], [0]]
h, w = 0, 0
for _ in range(6):
    a, leng = map(int, input().split())
    if a // 3:
        if leng > h: h = leng
    else:
        if leng > w: w = leng

    d.append(a)
    l.append(leng)

for i in range(5, -1, -1):
    if l[i] == 1:
        pass



    # x, y = field[0][-1], field[1][-1]
    # if a // 3:
    #     field.append((x, y + leng * d[a]))
    # else:
    #     field.append((x + leng * d[a], y))




'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''