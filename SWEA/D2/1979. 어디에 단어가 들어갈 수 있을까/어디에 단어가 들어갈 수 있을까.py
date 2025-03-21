T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    # n = 가로, 세로 길이
    # k = 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    # 조건을 만족하는 공간의 개수를 저장하는 변수
    answer = 0
    for i in range(n):
        # 연속된 1의 개수를 저장하는 변수
        count = 0

        # 행검사
        for j in range(n):
            # 흰색 부분은 1, 검정 부분은 0
            if puzzle[i][j] == 1:
                count += 1
            # 단어를 넣을 수 없는 칸을 만나거나 배열 끝에 도달했을 때 검사
            if puzzle[i][j] == 0 or j == n - 1:
                if count == k:
                    answer += 1
                count = 0

        # 열검사
        for j in range(n):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if count == k:
                    answer += 1
                count = 0
    print(f"#{test_case} {answer}")
