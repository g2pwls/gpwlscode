def dfs(index, calories, score):
    global max_score

    # 종료 조건: 모든 재료를 확인한 경우
    if index == N:
        max_score = max(max_score, score)
        return

    # 현재 재료를 선택하지 않는 경우
    dfs(index + 1, calories, score)

    # 현재 재료를 선택하는 경우 (칼로리 초과 X)
    Ti, Ki = ingredients[index]
    # 제한 칼로리와 같거나 낮으면
    if calories + Ki <= L:
        dfs(index + 1, calories + Ki, score + Ti)


# 입력 처리
T = int(input())
for t in range(1, T + 1):
    # N: 재료의 수, L: 제한 칼로리
    N, L = map(int, input().split())
    # 민기의 점수와 칼로리
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0  # 최대 맛 점수 초기화
    dfs(0, 0, 0)  # DFS 시작

    # 가장 점수가 높은 햄버거 점수
    print(f"#{t} {max_score}")
