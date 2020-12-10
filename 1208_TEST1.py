arr = input()

dic = {}
ch, cnt = 0, 0
for a in arr:
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1
    if dic[a] > cnt:
        ch, cnt = a, dic[a]

print(ch, cnt)
