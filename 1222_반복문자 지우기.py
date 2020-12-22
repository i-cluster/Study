# SWEA 4873
# https://bit.ly/34AKGCi

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    stg = input()

    stc = []
    print(f'#{tc} ', end='')
    for s in stg:
        if stc and stc[-1] == s: stc.pop()
        else: stc.append(s)
    else:
        print(len(stc))