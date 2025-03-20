T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 샘플에 숫자들을 미리 넣어둔다
    # 이따 계속 인덱스로 활용해야하기 때문
    sample = [2, 3, 5, 7, 11]
    # 나누고 나눈 값을 저장할 빈 리스트
    answer = []

    # sample 리스트의 길이 만큼 반복(5개만 확인해보면 되니까)
    for j in range(len(sample)):
        # N 나누기 sample[j]의 나머지가 0일때까지 반복
        while N % sample[j] == 0:
            # 나머지가 0이면 빈 리스트에 나눈 값을 저장
            answer.append(sample[j])
            # N을 N 나누기 sample[j]의 몫으로 다시 저장
            N = N // sample[j]

    # 각 숫자가 리스트에 몇 개씩 있는지 카운트
    a = answer.count(2)
    b = answer.count(3)
    c = answer.count(5)
    d = answer.count(7)
    e = answer.count(11)

    print(f"#{tc} {a} {b} {c} {d} {e}")
