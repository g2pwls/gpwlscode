from collections import deque

# 테스트 케이스 10개
T = 10

# 크기는 16x16 고정
N = 16

# 상하좌우 탐색을 위한 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, maze):
    # 방문 체크 배열 (0: 방문X, 1: 방문O)
    visited = [[0] * N for _ in range(N)]
    q = deque([(sr, sc)])
    visited[sr][sc] = 1  # 시작점 방문 표시

    while q:
        r, c = q.popleft()

        # 도착점(3)을 찾으면 도달 가능하므로 1 반환
        if maze[r][c] == 3:
            return 1

        # 상하좌우 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 갈 수 있는 곳인지 확인 (범위 내, 방문X, 벽X)
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != 1:
                q.append((nr, nc))
                visited[nr][nc] = 1  # 방문 표시

    return 0  # 도달할 수 없으면 0 반환

for tc in range(1, T + 1):
    # 테스트케이스 번호 입력 (사용하진 않지만 필요)
    input()

    # 미로 정보 입력
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 출발점 찾기
    sr, sc = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j

    # BFS 실행 후 결과 출력
    result = bfs(sr, sc, maze)
    print(f"#{tc} {result}")
