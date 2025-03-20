T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().strip()))

    max_count = 0
    count = 0

    for i in range(N):
        if arr[i] == 1:
            count += 1
            max_count = max(count, max_count)

        else:
            count = 0

    print(f"#{tc} {max_count}")