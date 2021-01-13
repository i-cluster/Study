# PROS 힙 42626
# https://bit.ly/3nwlJhP

import heapq


def solution(scoville, K):
    cnt, len_s = 0, len(scoville)
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len_s > 1:
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_2 * 2 + min_1)
            cnt += 1
            len_s -= 1
        else: return -1
    else: return cnt