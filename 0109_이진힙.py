# SWEA 5177
# https://bit.ly/39jZ3My

for tc in range(1, int(input())+1):
    n, heap = int(input()), [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        while heap[i] < heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i //= 2
    else:
        sum_nd = 0
        while n:
            sum_nd += heap[n // 2]
            n //= 2

    print(f'#{tc} {sum_nd}')