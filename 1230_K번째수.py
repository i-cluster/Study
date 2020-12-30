# PROS 정렬 42748
# https://bit.ly/2JsRHNV

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]