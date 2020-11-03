# https://www.acmicpc.net/problem/18406

N = input()
status = 0

for i in range(len(N)//2):
    status = status + int(N[i]) - int(N[-i-1])

print('READY' if status else 'LUCKY')