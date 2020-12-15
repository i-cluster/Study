# JO 3518
# https://bit.ly/2JQ1RbR

def qsort(s, e, pv):
    if e-s < 2:
        return arr[0]
    else:
        p, q = [], []
        for i in range(s, e-1):
            if arr[i] >= pv:
                q.append(arr[i])
            else:
                p.append(arr[i])
        arr[s:e] = p + [pv] + q

        for k in arr:
            print(k, end=' ')
        print()

        qsort(s, s + len(p), arr[s + len(p) - 1])
        qsort(s + len(p) + 1, e, arr[e - 1])


n = int(input())
arr = list(map(int, input().split()))

qsort(0, n, arr[-1])

'''
11
1 9 6 7 8 5 3 2 4 11 10
'''