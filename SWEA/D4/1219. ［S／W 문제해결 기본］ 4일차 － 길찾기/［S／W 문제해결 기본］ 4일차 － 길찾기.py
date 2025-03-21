def find_path(s, g):
    visited = [0] * 100  # 방문 체크 배열 (0~99)
    stack = []  # 돌아갈 곳을 저장할 스택

    while True:
        if visited[s] == 0:  # 첫 방문이면 체크
            visited[s] = 1

        for k in graph[s]:  # 현재 정점에서 이동할 수 있는 모든 정점 확인
            if visited[k] == 0:  # 방문하지 않은 정점이 있다면
                stack.append(s)  # 현재 위치 저장
                s = k  # 새로운 정점으로 이동
                break
        else:  # 더 이상 갈 곳이 없다면
            if stack:
                s = stack.pop()  # 이전 정점으로 되돌아감
            else:
                break  # 탐색 종료

    return visited


T = 10
for tc in range(1, T+1):
    tc_num, path_count = map(int, input().split())
    graph = [[] for _ in range(100)]  # 100개의 정점 생성

    edges = list(map(int, input().split()))
    for i in range(0, len(edges), 2):  # 순서쌍으로 변환
        start, end = edges[i], edges[i + 1]
        graph[start].append(end)  # 방향 그래프이므로 단방향 연결

    visited_lst = find_path(0, 99)  # 0에서 99까지 갈 수 있는지 확인

    result = 1 if visited_lst[99] == 1 else 0
    print(f'#{tc_num} {result}')
