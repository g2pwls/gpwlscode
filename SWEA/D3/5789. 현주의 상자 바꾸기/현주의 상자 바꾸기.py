T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 상자 만들어두기
    box = [0] * N

    # Q회 동안 반복
    for i in range(Q):
        L, R = map(int, input().split())

        # 리스트값 수정
        for bo in range(L-1, R):
            # i는 0부터 시작하기 때문에 +1 해줘야 함
            box[bo] = i+1

    print(f"#{tc}", *box)