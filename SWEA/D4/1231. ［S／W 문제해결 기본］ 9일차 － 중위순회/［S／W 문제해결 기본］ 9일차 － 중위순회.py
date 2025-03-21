def in_order(t):
    if t == 0:  # 자식 노드가 없을 경우 (더 이상 순회할 필요 없음)
        return

    # 왼쪽 자식 방문
    in_order(tree[t][1])
    # 현재 노드 문자 저장
    result.append(tree[t][0])
    # 오른쪽 자식 방문
    in_order(tree[t][2])


for tc in range(1, 11):
    N = int(input())  # 노드 개수
    tree = {}  # 트리 정보를 저장할 딕셔너리

    # 트리 정보 입력 받기
    for _ in range(N):
        data = input().split()
        node = int(data[0])  # 현재 노드 번호
        char = data[1]  # 저장된 문자
        left = int(data[2]) if len(data) > 2 else 0  # 왼쪽 자식 (없으면 0)
        right = int(data[3]) if len(data) > 3 else 0  # 오른쪽 자식 (없으면 0)
        tree[node] = (char, left, right)

    result = []  # 중위 순회 결과 저장 리스트
    in_order(1)  # 루트 노드부터 시작 (항상 1번이 루트)

    print(f"#{tc} {''.join(result)}")  # 출력
