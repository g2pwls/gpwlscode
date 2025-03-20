T = int(input())

for tc in range(1, T + 1):
    # N: 돌의 수, M: 뒤집기 횟수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        # i부터 j까지 반복
        for k in range(i - 1, i + j - 1):
            # 범위 벗어나지 않게 k값이 배열 길이보다 작으면
            if k < len(arr):
                # k값을 인덱스 i번째 돌색으로 변경
                arr[k] = arr[i - 1]

    print(f"#{tc}", *arr)
