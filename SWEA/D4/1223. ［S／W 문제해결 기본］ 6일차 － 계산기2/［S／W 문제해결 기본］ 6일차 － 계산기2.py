def infix_to_postfix(expression):
    precedence = {'+': 1, '*': 2}  # 연산자 우선순위 설정
    output = ""
    stack = []
    
    for char in expression:
        if char.isdigit():  # 피연산자라면 출력 문자열에 추가
            output += char
        else:  # 연산자인 경우
            while stack and precedence[stack[-1]] >= precedence[char]:
                output += stack.pop()
            stack.append(char)
    
    while stack:
        output += stack.pop()
    
    return output

def evaluate_postfix(postfix):
    stack = []
    
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '*':
                stack.append(a * b)
    
    return stack[0]

# 테스트 케이스 처리
for test_case in range(1, 11):
    _ = input().strip()  # 길이 입력 (사용하지 않음)
    expression = input().strip()
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    print(f"#{test_case} {result}")