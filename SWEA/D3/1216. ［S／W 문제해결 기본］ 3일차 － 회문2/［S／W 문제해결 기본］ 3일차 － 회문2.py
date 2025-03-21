N = 100
num = 10  # 테스트 케이스 개수

for tc in range(1, num + 1):
    num = input()  # 테스트 케이스 번호 (사용하지 않음)
    arr = [input().strip() for _ in range(N)]  # 100x100 글자판 입력

    max_length = 1  # 최소 회문 길이

    # 큰 길이부터 감소시키면서 찾기 (최대 길이 찾으면 탈출)
    for L in range(N, 1, -1):  # 100부터 2까지 감소하며 탐색
        found = False  # 현재 길이 L에서 회문을 찾았는지 여부

        # 가로 방향 검사
        for i in range(N):
            for j in range(N - L + 1):
                s = arr[i][j:j + L]  # 가로 문자열 추출
                if s == s[::-1]:  # 회문 검사
                    max_length = L
                    found = True
                    break
            if found:
                break  # 더 이상 작은 L을 검사할 필요 없음

        # 세로 방향 검사
        for j in range(N):
            for i in range(N - L + 1):
                s = ''.join(arr[i + k][j] for k in range(L))  # 세로 문자열 추출
                if s == s[::-1]:  # 회문 검사
                    max_length = L
                    found = True
                    break
            if found:
                break  # 더 이상 작은 L을 검사할 필요 없음

        if found:
            break  # 더 긴 회문을 찾았으므로 종료

    print(f"#{num} {max_length}")
