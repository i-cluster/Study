# SWEA 4012

def cook(a, b, k):
    if k < n:
        for i in range(n):
            pass
    else:
        print(a, b)
        # taste_a, taste_b = 0, 0
        # for i in range(n//2):
        #     for j in range(i+1, n//2):
        #         taste_a += taste[a[i]][a[j]] + taste[a[j]][a[i]]
        #         taste_b += taste[b[i]][b[j]] + taste[b[j]][b[i]]
        #
        # global min_taste
        # if min_taste > abs(taste_a - taste_b):
        #     min_taste = abs(taste_a - taste_b)


for tc in range(1, int(input())+1):
    n = int(input())
    taste = [list(map(int, input().split())) for _ in range(n)]

    elem = [i for i in range(n)]
    min_taste = 20000
    cook([], [], 0)

    print(f'#{tc} {min_taste}')


'''
1
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
'''