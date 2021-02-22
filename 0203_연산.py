# SWEA 5247
# https://bit.ly/2O0k4VK

def cal(n):
    ch = [0] * 1000001
    st, f = [n], 0
    ch[n] = 0
    while 1:
        n = st[f]
        for c in [1, -1, n, -10]:
            if n + c == m: return ch[n]+1
            if 0 <= n+c < 1000001 and not ch[n+c]:
                ch[n+c] = ch[n]+1
                st.append(n+c)
        f += 1


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    print(f'#{tc} {cal(n)}')