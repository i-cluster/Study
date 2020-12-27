# PROS 스택/큐
# https://bit.ly/3mL51e5

import sys
sys.stdin = open('sample.txt', 'r')


def solution(bridge_length, weight, truck_weights):
    on_bridge, cur_weight = [], 0
    truck_idx = 0
    cur_tm = 1

    while truck_idx < len(truck_weights):
        # 현재 시간에 하차해야 할 트럭이 있는 경우
        if on_bridge and on_bridge[0][1] == cur_tm:
            cur_weight -= on_bridge.pop(0)[0]

        # 다음 트럭 승차 시간으로 워프
        while cur_weight + truck_weights[truck_idx] > weight:
            truck = on_bridge.pop(0)
            cur_weight -= truck[0]
            cur_tm = truck[1]

        on_bridge.append((truck_weights[truck_idx], cur_tm + bridge_length))
        cur_weight += on_bridge[-1][0]
        truck_idx += 1
        cur_tm += 1

    return on_bridge[-1][1]


for tc in range(1, int(input())+1):
    bridge_length, weight = map(int, input().split())
    truck_weights = list(map(int, input().split()))
    print(f'#{tc} {solution(bridge_length, weight, truck_weights)}')
