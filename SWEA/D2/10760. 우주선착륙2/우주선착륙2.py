T = int(input())

# 상하좌우대각선 델타 방향
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최종 예비 후보지 결정 난 곳 개수
    place = 0

    for i in range(N):
        for j in range(M):
            # 시작점
            start = arr[i][j]
            # 예비후보지 개수 (본인보다 낮은 거 개수)
            land_place = 0
            # 8방향 탐색
            for d in range(8):
                # i, j: 현재 충선 위치
                # dr[d], dc[d]: 8방향 중 어느 방향인지
                ni = i + dr[d]
                nj = j + dc[d]
                # N x M 범위 안에 있는지 확인
                if 0 <= ni < N and 0 <= nj < M:
                    # 현재 내 위치보다 낮은 게 있으면
                    if start > arr[ni][nj]:
                        # 예비 후보지 개수 +1
                        land_place += 1
            # 예비 후보지 개수가 4 이상이면
            if land_place >= 4:
                # 최종 예비 후보지 +1
                place += 1

    print(f"#{tc} {place}")
