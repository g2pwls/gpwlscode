T = int(input())

for tc in range(1, T+1):
    # 10개의 수를 리스트로 입력 받는다.
    arr = list(map(int, input().split()))
    # 합의 값을 초기화해둔다.
    sum = 0

    # arr 리스트 안에 있는 값을 하나씩 뽑아서
    for i in arr:
        # 2로 나눈 나머지 값이 1이면
        if i % 2 == 1:
            # 그 값을 sum에 더한다
            sum += i

    print(f"#{tc} {sum}")