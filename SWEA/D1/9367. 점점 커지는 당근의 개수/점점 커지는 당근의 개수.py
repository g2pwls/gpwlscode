T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N = int(input())  # 당근 개수 입력
    N_list = list(map(int, input().split()))  # 당근 크기 리스트 입력

    count = 1  # 최소 길이는 1이므로 1로 시작
    max_count = 1  # 최대 연속 개수도 최소 1

    for i in range(1, N):  # 두 번째 요소부터 비교 시작
        if N_list[i] > N_list[i - 1]:  # 이전 값보다 크면 연속 증가
            count += 1
            max_count = max(max_count, count)  # 최대값 업데이트
        else:
            count = 1  # 연속 증가가 끊기면 다시 1로 초기화

    print(f"#{tc} {max_count}")  # 결과 출력