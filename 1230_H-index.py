# PROS 정렬 42747
# https://bit.ly/3o15IBA

def solution(citations):
    citations.sort(reverse=True)
    cnt = 0
    for ci in citations:
        if ci <= cnt: return cnt
        cnt += 1
    else: return cnt