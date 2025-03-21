T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]  # 2차원 리스트로 저장
    found = False  # 다섯 개 연속 여부 확인 변수

    # 가로 방향 검사
    for i in range(N):
        row = ''.join(board[i])  # 한 행을 문자열로 변환
        if 'ooooo' in row:
            found = True

    # 세로 방향 검사
    for j in range(N):
        col = ''.join(board[i][j] for i in range(N))  # j번째 열에서 i번째 행을 가져옴
        if 'ooooo' in col:
            found = True

    # 오른쪽 아래 대각선 검사
    for i in range(N - 4):
        for j in range(N - 4):
            diag = ''.join(board[i + k][j + k] for k in range(5)) # (i,j)부터 (i+4,j+4)까지 가져오기
            if diag == 'ooooo':
                found = True

    # 왼쪽 아래 대각선 검사
    for i in range(N - 4):
        for j in range(4, N):
            diag = ''.join(board[i + k][j - k] for k in range(5)) # (i,j)부터 (i+4,j-4)까지 가져오기
            if diag == 'ooooo':
                found = True

    # 결과 출력
    if found:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
