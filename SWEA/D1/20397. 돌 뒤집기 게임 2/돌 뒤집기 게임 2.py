T = int(input())

for tc in range(1, T + 1):
    # N: 돌의 수, M: 뒤집기 횟수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        # i번째 돌부터 j개의 돌을 비교하면서 뒤집기
        for x in range(1, j + 1):
            # 값들이 0과 N 사이에 존재해야한다.
            if 0 <= (i - 1 - x) < N and 0 <= (i - 1 + x) < N:
                # 대칭되는 둘이 같은지 확인
                if arr[i - 1 - x] == arr[i - 1 + x]:
                    # 1이면 0으로, 0이면 1로 뒤집기
                    arr[i - 1 - x] = 1 - arr[i - 1 - x]
                    arr[i - 1 + x] = 1 - arr[i - 1 + x]

    print(f"#{tc}", *arr)
