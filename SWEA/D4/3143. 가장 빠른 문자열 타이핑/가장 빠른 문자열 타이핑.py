T = int(input())

for tc in range(1, T + 1):
    text, pattern = input().split()

    # 패턴의 길이
    pl = len(pattern)
    # 텍스트의 길이
    tl = len(text)
    # 텍스트에서 가져올 글자의 위치
    ti = 0
    # 패턴이 사용된 횟수
    count = 0

    # 인덱스의 범위가 유효하면 계속 반복
    while ti < tl:
        pi = 0  # 패턴 비교 위치 초기화

        # 패턴과 일치하는지 확인
        while ti + pi < tl and pi < pl and text[ti + pi] == pattern[pi]:
            pi += 1

        # 패턴 전체를 찾은 경우
        if pi == pl:
            count += 1  # 패턴 사용 횟수 증가
            ti += pl  # 패턴 길이만큼 이동
        else:
            ti += 1  # 한 글자씩 이동

    # 최종 키 입력 횟수 계산
    result = tl - (count * (pl - 1))

    print(f"#{tc} {result}")
