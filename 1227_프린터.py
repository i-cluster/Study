# PROS 스택/큐
# https://bit.ly/3aM8hDB

def solution(priorities, location):
    answer = 0
    len_p = len(priorities)
    s = priorities.index(max(priorities))
    while answer < len_p:
        pr = max(priorities)
        for _ in range(len_p):
            if priorities[s] == pr:
                priorities[s] = 0
                answer += 1
                e = s
                if s == location:
                    return answer
            s = (s + 1) % len_p
        else:
            s = (e + 1) % len_p


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    priorities = list(map(int, input().split()))
    location = int(input())
    print(f'#{tc} {solution(priorities, location)}')