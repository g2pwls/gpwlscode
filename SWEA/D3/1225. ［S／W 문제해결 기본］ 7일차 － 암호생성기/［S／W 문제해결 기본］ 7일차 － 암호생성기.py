T = 10
N = 8  # 숫자 개수

for _ in range(T):
    test_case = int(input().strip())
    numbers = list(map(int, input().split()))
    
    q = [0] * (N + 1)  # 원형 큐 배열
    front = rear = 0  # 초기 front와 rear 위치 설정
    
    # 입력된 숫자를 원형 큐에 저장
    for num in numbers:
        rear = (rear + 1) % (N + 1)
        q[rear] = num
    
    number = 1  # 감소값 (1~5 반복)
    
    while True:
        front = (front + 1) % (N + 1)  # 첫 번째 원소 위치
        value = q[front] - number  # 감소 후 값 계산
        
        if value <= 0:
            value = 0  # 0 이하일 경우 0으로 고정
            rear = (rear + 1) % (N + 1)
            q[rear] = value
            break  # 종료 조건 만족 시 탈출
        
        rear = (rear + 1) % (N + 1)
        q[rear] = value  # 감소된 값을 맨 뒤로 이동
        
        number = 1 if number == 5 else number + 1  # 감소값 순환
    
    result = []
    for i in range(8):  # 최종 암호 8자리 추출
        front = (front + 1) % (N + 1)
        result.append(q[front])
    
    print(f"#{test_case}", *result)
