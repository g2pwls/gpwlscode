T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N x N 크기 리스트로 받기 공백없이 받기
    farm = [list(map(int, input().strip())) for _ in range(N)]

    # 중앙 좌표 찾기
    mid = N // 2
    # 곡식 수 초기화
    grain = 0

    # 마름모 모양으로 수확
    for i in range(N):
        # 왼쪽 범위: 왼쪽에서 몇칸 떨어져 있나
        start = abs(mid - i)
        # 오른족 범위: 왼쪽부터 몇칸까지 차있나
        end = N - start
        # 채워져있는 칸만 더하기
        grain += sum(farm[i][start:end])

    print(f"#{tc} {grain}")