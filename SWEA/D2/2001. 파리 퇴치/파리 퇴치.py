T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0

            for x in range(i, i+M):
                for y in range(j, j+M):
                    cnt += arr[x][y]

            if max_fly < cnt:
                max_fly = cnt
    print(f"#{tc} {max_fly}")