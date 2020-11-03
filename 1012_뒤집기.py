# https://www.acmicpc.net/problem/1439

S = input()
prev, cnt = S[0], 0
for i in S:
    if i != prev:
        cnt += 1
        prev = i

print(cnt//2 if S[0] == S[-1] else cnt//2 + 1)