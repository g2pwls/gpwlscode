def infix_to_postfix(expression):
    """중위 표기식을 후위 표기식으로 변환"""
    postfix = ""
    stack = []  # 연산자 스택

    for char in expression:
        if char.isdigit():
            postfix += char  # 숫자는 그대로 추가
        elif char == '+':
            while stack:
                postfix += stack.pop()  # 기존 연산자 꺼내기
            stack.append(char)  # 새로운 연산자 추가

    while stack:
        postfix += stack.pop()  # 남은 연산자 추가

    return postfix


def evaluate_postfix(postfix):
    """후위 표기식을 계산"""
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))  # 숫자는 스택에 추가
        elif char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)  # b + a 순서로 계산

    return stack[0]  # 최종 결과 반환


# 10개의 테스트 케이스 실행
T = 10
for tc in range(1, T + 1):
    n = int(input())  # 계산식 길이 입력 (사용하지 않음)
    infix = input().strip()  # 중위 표기식 입력

    postfix = infix_to_postfix(infix)
    result = evaluate_postfix(postfix)

    print(f"#{tc} {result}")
