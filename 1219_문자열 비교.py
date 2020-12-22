# SWEA 4864
# https://bit.ly/3rcJChh

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    str1, str2 = input(), input()
    len1 = len(str1)

    print(f'#{tc} ', end='')
    i = len1 - 1
    while i < len(str2):
        if str2[i] == str1[-1]:
            for k in range(1, len1):
                if str2[i-k] != str1[-1-k]: i += 1; break
            else:
                print(1); break
        elif str2[i] in str1:
            for k in range(1, len1):
                if str1[-1-k] == str2[i]: i += k; break
        else:
            i += len1
    else: print(0)