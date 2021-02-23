# SWEA 5248
# https://bit.ly/2O0k4VK

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    apply = list(map(int, input().split()))

    team = [0] * (n+1)
    team_no, overlap = 0, 0
    for k in range(m):
        i, j = apply[k*2], apply[k*2+1]
        if not team[i] and not team[j]:
            team_no += 1
            team[i] = team[j] = team_no
        elif min(team[i], team[j]) == 0:
            team[i] = team[j] = team_no
        else:
            if team[i] != team[j]: overlap += 1

    print(f'#{tc} {team_no - overlap + team.count(0) - 1}')