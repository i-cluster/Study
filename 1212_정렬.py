# JO 1146, JO 1158, JO 1157
# https://bit.ly/2W2r2dy, https://bit.ly/2Wd24IB, https://bit.ly/37Zd6Xl

n = int(input())
arr = list(map(int, input().split()))

# 선택정렬
for i in range(n-1):
    minI = arr[i:].index(min(arr[i:])) + i
    arr[i], arr[minI] = arr[minI], arr[i]
    for a in arr:
        print(a, end=' ')
    print()

# 삽입정렬
for i in range(1, n):
    for k in range(i):
        if arr[k] > arr[i]:
            arr[:i+1] = arr[:k] + [arr[i]] + arr[k:i]
            for a in arr:
                print(a, end=' ')
            print()
            break
    else:
        for a in arr:
            print(a, end=' ')
        print()

# 버블정렬
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        for a in arr:
            print(a, end=' ')
        print()