# SWEA 5658

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    nums = input()
    n //= 4

    # 비밀번호 배열
    pw = []
    for _ in range(n):
        # 숫자 4개를 비밀번호 배열에 저장
        for i in range(4):
            num = nums[i * n:i * n + n]
            if num not in pw:
                pw.append(num)
        # 배열 맨 뒤 숫자를 앞으로 가져오기
        nums = nums[-1] + nums[:-1]

    # 내림차순 정렬
    pw.sort(reverse=True)

    print(f'#{tc} {int("0x"+pw[k-1], 16)}')