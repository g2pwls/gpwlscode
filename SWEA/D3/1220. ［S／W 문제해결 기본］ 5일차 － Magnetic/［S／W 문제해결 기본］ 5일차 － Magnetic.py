for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 교착 상태 개수
    count = 0

    # 각 열 기준 탐색
    # 자석은 세로로 영향을 받음 행은 필요 x
    for i in range(N):
        # 교착상태 시작됐는지 아닌지 확인
        stuck = False
        for j in range(N):
            # 만약 N극이면
            if arr[j][i] == 1:
                # 교착상태 시작
                stuck = True
            # 만약 S극이고 교착상태가 시작되었으면
            elif arr[j][i] == 2 and stuck:
                # 교착 상태 개수 증가
                count += 1
                # 새로운 교착 상태 찾아야하기 때문에 초기화
                stuck = False

    print(f"#{tc} {count}")