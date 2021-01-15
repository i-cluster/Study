# SWEA 5178
# https://bit.ly/39jZ3My

def find_leaf(k):
    if k*2+1 <= n: find_leaf(k*2); find_leaf(k*2+1)
    elif k*2 <= n: find_leaf(k*2)
    else: global sum_nd; sum_nd += dic[k]


for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    dic, sum_nd = {}, 0
    for _ in range(m):
        a, b = map(int, input().split())
        dic[a] = b

    find_leaf(l)
    print(f'#{tc} {sum_nd}')