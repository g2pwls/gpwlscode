T = 10

for tc in range(1, T+1):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    # 각 행의 합
    for i in range(100):
        row_sum = sum(arr[i])
        max_sum = max(max_sum, row_sum)

    # 각 열의 합
    for j in range(100):
        col_sum = sum(arr[i][j] for i in range(100))
        max_sum = max(max_sum, col_sum)

    # 대각선 합 (왼 위 -> 오 아)
    diag1_sum = sum(arr[i][i] for i in range(100))
    max_sum = max(max_sum, diag1_sum)

    # 대각선 합 (오 위 -> 왼 아)
    diag2_sum = sum(arr[i][99-i] for i in range(100))
    max_sum = max(max_sum, diag2_sum)

    print(f"#{tc} {max_sum}")