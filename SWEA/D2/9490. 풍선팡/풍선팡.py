T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 델타 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 최대값 초기화
    max_pop = 0

    # 모든 풍선 탐색
    # 전체 N x M 풍선을 모두 확인해야하니까 이중 반복문 사용
    for i in range(N):
        for j in range(M):
            # 현재 풍선을 터뜨렸을 때의 값을 저장
            total = arr[i][j]

            # 풍선의 값만큼 확장해야하기 때문
            for r in range(1, arr[i][j]+1):
                # 4방향 탐색해야함
                for d in range(4):
                    # i: 현재 충선 위치
                    # dr[d]: 4방향 중 어느 방향인지
                    # r: 얼마나 멀리 영향을 미치는지
                    ni = i + dr[d] * r
                    nj = j + dc[d] * r

                    # N x M 범위 안에 있는지 확인
                    if 0 <= ni < N and 0 <= nj < M:
                        # 범위 안에 있으면 더하기
                        total += arr[ni][nj]

                # 최댓값보다 토탈이 크면 변경
                if max_pop < total:
                    max_pop = total

    print(f"#{tc} {max_pop}")
