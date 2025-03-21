T = 10 #테스트 케이스 개수

for tc in range(1,T+1): #1부터 10까지 반복
    N = int(input()) # 덤프 횟수
    arr = list(map(int, input().split()))  # 각 상자의 높이값
    for j in range(N): # 덤프 횟수만큼 반복
        maxval = max(arr) # 상자들 중 가장 높은 상자 maxval에 저장
        minval = min(arr) # 상자들 중 가장 낮은 상자 minval에 저장

        # 평탄화가 완료되었으면 더 이상 덤프 안함
        if maxval - minval <= 1:
            break

        minindex = arr.index(minval) # 가장 높은 상자 인덱스 번호 저장
        maxindex = arr.index(maxval) # 가장 낮은 상자 인덱스 번호 저장
        arr[minindex] += 1 # 낮은 상자 인덱스 1 추가
        arr[maxindex] -= 1 # 높은 상자 인덱스 1 빼기
    result = max(arr) - min(arr) # 반복문 다 돌고나서 가장 높은 상자 - 가장 낮은 상자
    print(f"#{tc} {result}")