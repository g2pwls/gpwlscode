T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N: 배열 크기
    # M: 스프레이의 세기

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 잡을 수 있는 파리 수
    max_fly = 0

    # 상하좌우 델타탐색 1번
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 대각선 4방향 델타탐색 2번
    di = [-1, -1, 1, 1]
    dj = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            s1 = arr[i][j]
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                for c in range(1, M):
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]

                if max_fly < s1:
                    max_fly = s1

    for i in range(N):
        for j in range(N):
            s2 = arr[i][j]

            for di, dj in [[-1, 1], [-1, -1], [1, -1], [1, 1]]:
                for k in range(1, M):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        s2 += arr[ni][nj]
            if max_fly < s2:
                max_fly = s2

    # 그중에 최대값 구해서 출력
    print(f"#{tc} {max_fly}")
