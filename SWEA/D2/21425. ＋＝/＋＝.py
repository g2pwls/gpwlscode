T = int(input())

for tc in range(1, T+1):
    A, B, N = map(int, input().split())

    count = 0

    while True:
        if B > A:
            count += 1
            A += B
        else:
            count += 1
            B += A

        if A > N or B > N:
            break

    print(count)