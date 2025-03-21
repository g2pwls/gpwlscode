T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, Q = map(int, input().split())  # N: 상자 개수, Q: 작업 개수
    boxes = [0] * N  # 처음에는 모든 상자가 0

    # Q번의 작업 수행
    for i in range(1, Q + 1):
        L, R = map(int, input().split())  # 범위 입력
        for j in range(L - 1, R):  # 인덱스 조정 (1-based -> 0-based)
            boxes[j] = i  # i번째 작업 번호로 업데이트

    # 결과 출력
    print(f"#{tc}", *boxes)