# # https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
#
# def check(lock_count):
#     # 열쇠 인덱스
#     for i in range(-m+1, n):
#         for j in range(-m+1, n):
#             # 열쇠 크기 -> 자물 탐색
#             count = lock_count
#             for p in range(m):
#                 keep = True
#                 for q in range(m):
#                     if 0 <= i+p < n and 0 <= j+q < n:
#                         k, l = key[i+p][j+q], lock[i+p][j+q]
#                         # 돌기끼리 만나면 탐색 종료
#                         if k and l: keep = False; break
#                         # 열쇠 돌기와 자물쇠 홈
#                         if k and not l: count -= 1
#                 else:
#                     if not count: return 1
#                 if not keep: break
#
#
# def turning():
#     global key
#     turned_key = [[0] * 3 for _ in range(m)]
#     for i in range(m):
#         for j in range(m):
#             turned_key[j][m-1-i] = key[i][j]
#     key = turned_key
#
#
# m, n = 3, 3
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# lock_count = sum(l.count(0) for l in lock)
#
# if check(lock_count):
#     print(True)
# else:
#     for i in range(3):
#         turning()
#         if check(lock_count):
#             print(True)
#             break
#     else:
#         print(False)


def solution(key, lock):
    m, n = len(key), len(lock)
    lock_count = sum(l.count(0) for l in lock)
    answer = False

    if check(m, n, key, lock, lock_count):
        answer = True
    else:
        for _ in range(3):
            key = turning(key, m)
            if check(m, n, key, lock, lock_count):
                answer = True
                break

    return answer


def check(m, n, key, lock, lock_count):
    # 열쇠 인덱스
    for i in range(-m + 1, n):
        for j in range(-m + 1, n):
            # 열쇠 크기 -> 자물 탐색
            count = lock_count
            for p in range(m):
                keep = True
                for q in range(m):
                    if 0 <= i + p < n and 0 <= j + q < n:
                        k, l = key[p][q], lock[i + p][j + q]
                        # 돌기끼리 만나면 탐색 종료
                        if k and l: keep = False; break
                        # 열쇠 돌기와 자물쇠 홈
                        if k and not l: count -= 1
                else:
                    if not count: return 1
                if not keep: break


def turning(key, m):
    turned_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            turned_key[j][m-1-i] = key[i][j]
    key = turned_key
    return key