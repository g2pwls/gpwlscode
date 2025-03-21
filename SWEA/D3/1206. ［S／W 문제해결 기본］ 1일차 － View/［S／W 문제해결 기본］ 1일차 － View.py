for test_case in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        left = max(B[i-1], B[i-2])
        right = max(B[i+1], B[i+2])
        best = max(left, right)
        if B[i] > best:
            result += B[i]-best
    print(f"#{test_case} {result}")