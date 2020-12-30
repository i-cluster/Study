# PROS 정렬 42746
# https://bit.ly/2L1DLLk

def sorting(strs, l, h):
    if l < h:
        i = l - 1
        pv = strs[h]

        for j in range(l, h):
            if strs[j] + pv > pv + strs[j]:
                i += 1
                strs[i], strs[j] = strs[j], strs[i]

        strs[i + 1], strs[h] = strs[h], strs[i + 1]

        sorting(strs, l, i)
        sorting(strs, i + 2, h)


def solution(numbers):
    strs = list(str(n) for n in numbers)
    sorting(strs, 0, len(strs) - 1)

    answer = ''.join(strs).lstrip('0')
    return answer if answer else '0'