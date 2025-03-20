T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 유물들 길이를 저장할 빈 리스트
    relics = []

    # 가로 검사
    for r in range(N):
        # 유물 길이
        length = 0
        for c in range(M):
            # 가로 검사하는데 1이면
            if arr[r][c] == 1:
                # 유물 길이 1 증가
                length += 1
            # 0을 만났을 때
            else:
                # 만약 유물길이가 2 이상이면
                if length >= 2:
                    # 유물 길이 리스트에 길이 추가
                    relics.append(length)
                # 0 만나서 유물 끝이니까 다시 초기화
                length = 0
        # 마지막까지 1이 지속된 경우 추가
        if length >= 2:
            relics.append(length)

    # 세로 검사
    for c in range(M):
        # 유물 길이
        length = 0
        for r in range(N):
            # 세로 검사하는데 1이면
            if arr[r][c] == 1:
                # 유물 길이 1 증가
                length += 1
            else:
                # 만약 유물길이가 2 이상이면
                if length >= 2:
                    # 유물 길이 리스트에 길이 추가
                    relics.append(length)
                length = 0
        # 마지막까지 1이 지속된 경우 추가
        if length >= 2:
            relics.append(length)

    # 리스트 값 중 최대 값 출력
    print(f"#{tc}", max(relics))
