T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 양의 숫자들을 넣을 빈 리스트 생성
    dream = []
    # i를 1로 초기화
    i = 1

    # dream 리스트에 있는 숫자들을 중복 제거하고 개수 센다
    # 그 개수가 10개가 될 때까지 반복: 중복제거
    # 리스트에 0~9까지 다 있을 때까지 반복
    # 11, 23과 같은 두 자리 수도 1,1,2,3 이렇게 저장됨
    # 그래서 0~9까지 다 들어왔는지 판단할 수 있음
    while len(set(dream)) < 10:
            # 양의 수 계산
            sheep = N * i
            # 양의 수를 문자열로 변환
            # 각 자리수를 리스트에 하나씩 추가
            dream.extend(str(sheep))
            i += 1

    print(f"#{tc} {sheep}")

