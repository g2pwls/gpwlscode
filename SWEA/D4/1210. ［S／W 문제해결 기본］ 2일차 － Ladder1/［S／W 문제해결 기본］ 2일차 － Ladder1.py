def find_start_x(ladder):
    # 도착점(2) 찾기
    x = ladder[99].index(2)  # 마지막 행에서 2의 위치 찾기
    y = 99  # 가장 아래에서 출발

    # 이동 방향 (왼쪽, 오른쪽, 위쪽)
    dx = [-1, 1, 0]  # x 방향 이동 (좌, 우, 위)
    dy = [0, 0, -1]  # y 방향 이동 (좌, 우, 위)

    # 위로 올라가면서 탐색
    while y > 0:
        for d in range(2):  # 좌(0) -> 우(1) 먼저 확인
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 100 and ladder[ny][nx] == 1:
                # 좌/우로 이동 가능하면 끝까지 이동
                while 0 <= nx < 100 and ladder[ny][nx] == 1:
                    x = nx  # 이동
                    nx += dx[d]  # 같은 방향으로 계속 이동
                break  # 좌/우 이동 후에는 위로 올라가야 하므로 탈출

        # 위로 이동
        y += dy[2]  # dy[2] = -1 이므로 위로 이동

    return x  # 도착한 x 값 반환

for _ in range(10):  # 테스트 케이스 10개
    test_case = int(input())  # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 100x100 사다리 입력

    result = find_start_x(ladder)
    print(f"#{test_case} {result}")
