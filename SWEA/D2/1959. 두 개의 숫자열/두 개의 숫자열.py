T = int(input())

for tc in range(1, T+1):
    # N: Aj 숫자열의 길이
    # M: Bh 숫자열의 길이
    N, M = map(int,input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 음의 무한대로 초기화
    max_v = float('-inf')
    # Aj가 항상 긴 배열이 되도록
    if N < M:
        N, M = M, N
        Aj, Bj = Bj, Aj
    # if N > M인 경우에 대한 코드
    # 움직일 수 있는 기준
    for i in range(N-M+1):
        # 마주보는 원소들 곱의 합
        sum_value = 0
        # 짧은 배열에서 비교하는 위치
        for j in range(M):
            # 서로 마주보는 숫자들을 곱한 뒤 합
            sum_value += Aj[i+j] * Bj[j]
            # 합이 음수보다 크면 max값으로 저장
        if max_v < sum_value:
            max_v = sum_value

    print(f"#{tc} {max_v}")