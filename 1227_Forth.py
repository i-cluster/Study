# SWEA 4874
# https://bit.ly/37RsQgj

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    arr = list(input().split())
    res = 0

    print(f'#{tc} ', end='')
    cal = []
    for a in arr[:-1]:
        if a not in ('+', '*', '-', '/'):
            cal.append(int(a))
        else:
            if len(cal) >= 2:
                y, x = int(cal.pop()), int(cal.pop())
                if a == '+': cal.append(x + y)
                elif a == '*': cal.append(x * y)
                elif a == '-': cal.append(x - y)
                else: cal.append(x // y)
            else:
                print('error')
                break
    else:
        if len(cal) == 1: print(cal[0])
        else: print('error')