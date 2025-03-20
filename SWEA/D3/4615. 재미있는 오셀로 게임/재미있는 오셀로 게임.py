T = int(input())

# 8방향 탐색 (상,하,좌,우,대각선)
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 보드 초기화
    board = [[0] * N for _ in range(N)]
    # 중앙에 흑돌, 백돌 놔야하기 때문에 중앙 찾기
    mid = N // 2
    # 계산해서 흑돌, 백돌 자리 찾아주기
    white = board[mid][mid] = board[mid - 1][mid - 1] = 2
    black = board[mid - 1][mid] = board[mid][mid - 1] = 1

    # M번 돌 놓기
    for _ in range(M):
        x, y, color = map(int, input().split())
        # 인덱스이기 때문에 미리 -1 빼서 선언
        x -= 1
        y -= 1
        board[x][y] = color

        # 돌 뒤집기 (8방향 탐색)
        for d in range(8):
            # 현재 위치에서 특정방향으로 한 칸 이동
            nx, ny = x+dx[d], y+dy[d]
            # 뒤집을 후보 리스트
            change = []

            # 방향 탐색하면서 상대돌 있나 탐색
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == (3 - color):
                # 상대돌 있으면 뒤집을 후보 위치를 리스트에 추가
                change.append((nx, ny))
                # 계속 이동하면서 탐색
                nx += dx[d]
                ny += dy[d]

            # 탐색이 끝나고
            # 만약 현재 위치에 내 돌 있으면 리스트에 저장된 상대 돌 뒤집기
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                # 리스트에 저장된 좌표를 반복하여 돌 뒤집기
                for px, py in change:
                    board[px][py] = color

    # 흑돌, 백돌 개수 세기
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1

    print(f"#{tc} {b_cnt} {w_cnt}")