T = int(input())

for tc in range(1, T+1):
    N = int(input())
    is_possible = False

    # 이중 for문을 활용해서 모든 경우 비교
    for a in range(1, 10):
        for b in range(1, 10):
            # 곱하기 가능하면
            if N == a * b:
                # 가능하면 True
                is_possible = True
                # 내부 for문 탈출
                break
        # 외부 for문 탈출
        if is_possible:
            break

    # is_possible이 True면 Yes 출력
    # is_possible이 False면 No 출력
    print(f"#{tc} {'Yes' if is_possible else 'No'}")
