T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    N, K = map(int, input().split())  # N개의 숫자, 목표 합 K
    A = list(map(int, input().split()))  # 수열 A
    count = 0  # 합이 K가 되는 경우의 수
    
    stack = [(0, 0)]  # (현재 인덱스, 현재까지의 합)을 저장하는 스택
    
    while stack:
        idx, current_sum = stack.pop()
        
        # 배열 범위를 벗어나면 탐색 종료
        if idx >= N:
            continue

        # 현재 원소를 선택하는 경우
        if current_sum + A[idx] == K:
            count += 1
        elif current_sum + A[idx] < K:  # K보다 작을 때만 탐색 (불필요한 탐색 방지)
            stack.append((idx + 1, current_sum + A[idx]))
        
        # 현재 원소를 선택하지 않는 경우
        stack.append((idx + 1, current_sum))
    
    print(f'#{t} {count}')
