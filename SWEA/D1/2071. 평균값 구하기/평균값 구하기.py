T = int(input())

for tc in range(1, T+1):
    # 10개의 수를 리스트로 입력 받는다.
    arr = list(map(int, input().split()))
    # 합의 값을 초기화해둔다.
    sum = 0

    # arr 리스트 안에 있는 값을 하나씩 뽑아서
    for i in arr:
        # 그 값들을 다 저장한다.
        sum += i

    # 리스트 값의 합을 리스트의 길이로 나눠서 평균을 구한다.
    avg = sum / len(arr)

    # 소수점 첫째 자리에서 반올림한다.
    print(f"#{tc} {avg:.0f}")