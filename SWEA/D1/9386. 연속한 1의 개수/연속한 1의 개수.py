T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 수열을 공백 없이 받기
    arr = list(map(int, input().strip()))

    # 최대 카운트값을 초기화
    max_count = 0
    # 카운트값을 초기화
    count = 0

    # 수열길이만큼 반복
    for i in range(N):
        # 만약 수열 값이 1이면
        if arr[i] == 1:
            # 카운트 1 증가
            count += 1
            # 최대카운트 값을 카운트값과 최대카운트값 중 더 큰 것으로 변경
            max_count = max(count, max_count)

        # 수열 값이 0이 아니면
        else:
            # 카운트 값을 0으로
            count = 0

    print(f"#{tc} {max_count}")