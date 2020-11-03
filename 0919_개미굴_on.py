# https://www.acmicpc.net/problem/14725

n = int(input())
# cave = [ 굴 깊이 idx [(먹이, 상위 굴 먹이, 상위 굴 번호)] ]
# cave = [(먹이, 하위 굴 번호)] index는 굴 번호
cave = {[]}

# 굴 번호 id
id = 0
for _ in range(n):
    arr = list(input().split())
    # cave 꼭대기부터 하나씩 넣기
    for i in range(1, int(arr[0])+1):
        # 층 정보가 있으면
        pass
        # 층 정보가 없으면
        pass
