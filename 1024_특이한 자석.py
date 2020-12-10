# SWEA 4013, 모의 역량 테스트

def spin(n, d):
    # 자석 회전 기록하기
    v[n] = 1
    # 우측 자석의 회전 기록이 없고 접점 자석 극이 반대인 경우
    if n < 4 and not v[n + 1] and magnet[n][key[n] - 6] != magnet[n + 1][key[n + 1] - 2]:
        # 우측 자석을 반대 방향으로 회전
        spin(n + 1, -d)
    # 좌측 자석의 회전 기록이 없고 접점 자석 극이 반대인 경우
    if n >= 2 and not v[n - 1] and magnet[n][key[n] - 2] != magnet[n - 1][key[n - 1] - 6]:
        # 좌측 자석을 반대 방향으로 회전
        spin(n - 1, -d)

    # 회전 방향과 거리만큼 키 이동
    key[n] = (key[n] + (-1) * d) % 8


for tc in range(1, int(input()) + 1):
    k = int(input())
    magnet = [''] + [list(map(int, input().split())) for _ in range(4)]
    # 자석 맨 위의 위치 정보
    key = [0] * 5

    for _ in range(k):
        n, d = map(int, input().split())
        # 자석 회전 기록
        v = [0] * 5
        # 자석 회전
        spin(n, d)

    score = 0
    for i in range(1, 5):
        if magnet[i][key[i]]:
            score += 2 ** (i - 1)

    print(f'#{tc} {score}')