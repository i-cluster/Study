# SWEA 5174
# https://bit.ly/39jZ3My

def subtree(n):
    if n:
        global cnt
        cnt += 1
        subtree(tree[n][0])
        subtree(tree[n][1])

    return cnt


for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(e+2)]

    for i in range(e):
        a, b = arr[i*2], arr[i*2+1]
        if tree[a][0]: tree[a][1] = b
        else: tree[a][0] = b

    cnt = 0

    print(f'#{tc} {subtree(n)}')
