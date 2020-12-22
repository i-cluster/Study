# SWEA 4865
# https://bit.ly/2KoHWkp

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    str1, str2 = input(), input()

    dic, max_c = {}, 0
    for s1 in str1:
        if s1 not in dic.keys():
            for s2 in str2:
                if s1 == s2:
                    if s1 in dic.keys(): dic[s1] += 1
                    else: dic[s1] = 1

                    if dic[s1] > max_c: max_c = dic[s1]

    print(f'#{tc} {max_c}')