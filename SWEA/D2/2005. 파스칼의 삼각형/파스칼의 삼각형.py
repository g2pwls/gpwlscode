def pascal(n):
    """크기 n인 파스칼 삼각형을 재귀적으로 생성"""
    if n == 1:
        return [[1]]  # 첫 번째 줄은 항상 [1]
    
    prev_triangle = pascal(n - 1)  # 이전 삼각형을 재귀적으로 구함
    prev_row = prev_triangle[-1]  # 이전 삼각형의 마지막 행
    new_row = [1]  # 새 행의 첫 번째 요소는 1

    for i in range(1, len(prev_row)):  
        new_row.append(prev_row[i] + prev_row[i - 1])  # 이전 행의 두 수를 더해 중간 값 생성

    new_row.append(1)  # 새 행의 마지막 요소는 1
    prev_triangle.append(new_row)  # 삼각형에 새 행 추가

    return prev_triangle

# 입력 및 출력 처리
T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    N = int(input())  # 파스칼의 삼각형 크기
    triangle = pascal(N)

    print(f"#{t}")  # 테스트 케이스 번호 출력
    for row in triangle:
        print(" ".join(map(str, row)))  # 공백으로 구분하여 출력
