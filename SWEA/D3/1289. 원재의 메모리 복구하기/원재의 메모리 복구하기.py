T = int(input())

for tc in range(1, T+1):
    memo = list(map(int, input().strip()))
    count = 0

    # 리스트의 길이만큼 반복
    for i in range(len(memo)):
        # 만약 memo[i]의 값이 1이라면
        if memo[i] == 1:
            # 카운트 1 증가
            count += 1

            # 그 i부터 리스트의 끝까지
            for j in range(i, len(memo)):
                # 숫자 반대로 변경 1이면 0, 0이면 1
                memo[j] = 1 - memo[j]

    print(f"#{tc} {count}")