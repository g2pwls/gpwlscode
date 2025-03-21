# 2차원 배열의 크기 N*N
N = 8

T = 10
for tc in range(1, T+1):
    # 우리가 찾아야하는 회문의 길이 M
    M = int(input())
    # 8 x 8 크이긔 글자판 입력 받기
    arr = [input() for _ in range(N)]

    # 회문의 개수 (답)
    count = 0

    # 모든 위치에서 시작해서 길이가 M인 회문을 만들어 봐라
    # 행 번호: i, 열 번호: j
    # 모든 위치(1,j) 에서 회문을 만들어 본다. 길이 M 짜리
    # (i,j) ~ (i, j + M) => 가로 문자열 하나 만들어서 회문인지 판단
    # 행 우선순위
    for i in range(N): # 각 행을 탐색
        for j in range(N-M+1): # 길이 M 만큼 확인할 수 있는 시작점까지만 검사
            s = arr[i][j:j+M] # 가로 문자열 생성
            for k in range(M // 2): # 문자열의 앞과 뒤 비교 (회문)
                if s[k] != s[M - 1 - k]:
                    break # 회문이 아니면
            else:
                count += 1 # 회문이면

    # (i,j) ~ (i + M, j) => 세로 문자열 하나 만들어서 회문인지 판단
    # 열 우선순위
    for j in range(N): # 각 열을 탐색
        for i in range(N - M + 1): # 길이 M만큼 확인할 수 있는 시작점까지만 검사
            s = ''.join(arr[i+k][j] for k in range(M)) # 세로 문자열 생성
            for k in range(M // 2):
                if s[k] != s[M - 1 - k]:
                    break
            else:
                count += 1

    print(f"#{tc} {count}")