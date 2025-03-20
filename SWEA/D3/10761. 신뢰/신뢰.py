T = int(input())

for tc in range(1, T + 1):
    # 한 줄 입력받아서 공백 기준으로 나누기
    arr = input().split()
    # 버튼을 누르는 개수
    N = int(arr[0])
    # 실제 버튼 누르는 순서들
    commands = arr[1:]

    # 로봇들의 시작 위치
    o_position, b_position = 1, 1
    # 각 로봇이 버튼을 누르기까지 걸린 시간
    o_time, b_time = 0, 0

    for i in range(N):
        robot = commands[2 * i]
        # 타겟 버튼
        target = int(commands[2 * i + 1])

        if robot == 'O':  # 오렌지 로봇이 버튼을 누르는 경우
            # 목표 위치까지 이동하는 데 걸리는 시간
            # 타겟 버튼 위치 - 현재 로봇 위치
            move_time = abs(target - o_position)
            # o_time + move_time: 오렌지 로봇이 이동하는 데 걸리는 시간
            # b_time: 블루 로봇이 최근에 버튼을 누른 시간
            # 오렌지 로봇이 버튼을 누르려면 최소한 블루 로봇이 버튼을 누른 이후여야 함
            # 버튼 누르는데 1초 추가
            o_time = max(o_time + move_time, b_time) + 1
            # 버튼을 누른 후 현재 위치 업데이트
            o_position = target
        else:  # 블루 로봇이 버튼을 누르는 경우
            # 목표 위치까지 이동하는 데 걸리는 시간
            # 타겟 버튼 위치 - 현재 로봇 위치
            move_time = abs(target - b_position)
            # b_time + move_time: 블루 로봇이 이동하는 데 걸리는 시간
            # o_time: 오렌지 로봇이 최근에 버튼을 누른 시간
            # 블루 로봇이 버튼을 누르려면 최소한 오렌지 로봇이 버튼을 누른 이후여야 함
            # 버튼 누르는데 1초 추가
            b_time = max(b_time + move_time, o_time) + 1
            # 버튼을 누른 후 현재 위치 업데이트
            b_position = target

    print(f"#{tc} {max(o_time, b_time)}")
