# https://www.acmicpc.net/problem/1244

n = int(input())
switch = [0] + list(map(int, input().split()))
len_s = len(switch) - 1

m = int(input())
for _ in range(m):
    # 성별 s, 번호 k
    s, k = map(int, input().split())

    # 남자라면
    if s == 1:
        # 몫 * 번호로 이동하며 바꾸기
        for i in range(1, len_s // k + 1):
            switch[i*k] = 1 - switch[i*k]
    # 여자라면
    else:
        # 현재 번호 바꾸기
        switch[k] = 1 - switch[k]
        # 앞뒤로 이동 가능한 거리 중 짧은 쪽으로 이동
        for j in range(1, min(k, len_s-k+1)):
            # 한칸씩 앞뒤로 이동하며 같으면 바꾸기
            if switch[k-j] == switch[k+j]:
                switch[k-j] = switch[k+j] = - switch[k-j] + 1
            else: break

for i in range(1, n+1):
    if i % 20:
        print(switch[i], end=' ')
    else:
        print(switch[i])