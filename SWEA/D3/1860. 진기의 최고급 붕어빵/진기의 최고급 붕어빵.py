T = int(input())

for tc in range(1, T+1):
    # N: 사람 수, M: 생산 시간, K: 한번에 만드는 개수
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    # 손님이 도착하는 순서대로 처리하기 위해 정렬
    arrive_time.sort()

    # 기본 상태: 가능
    state = 'Possible'
    for i in range(N):
        time = arrive_time[i]
        # 특정 시간까지 만들어진 붕어빵 개수 세기
        # (도착시간 // 생산 시간) = 붕어빵 만든 횟수
        # (붕어빵 만든 횟수) * 한 번에 만들어지는 개수 = 만들어진 총 붕어빵 개수
        bread = (time // M) * K

        # 사람수보다 빵이 작으면 실패
        if bread < (i+1):
            state = 'Impossible'
            break

    print(f"#{tc} {state}")