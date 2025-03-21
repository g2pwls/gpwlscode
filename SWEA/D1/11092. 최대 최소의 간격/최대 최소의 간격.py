T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    # 최대값, 최소값 초기화
    max_value = ai[0]
    min_value = ai[0]

    # 위치값 초기화
    max_index = 0
    min_index = 0

    for i in range(N):
        if ai[i] < min_value:
            min_value = ai[i]
            min_index = i
        if ai[i] >= max_value:
            max_value = ai[i]
            max_index = i

    result = abs(max_index - min_index)

    print(f"#{tc} {result}")