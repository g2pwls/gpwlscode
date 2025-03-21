T = 10

for tc in range(1, T+1):
    n = int(input())
    # 괄호검사 할 문자열
    check = input()
    # 우리가 사용할 빈 스택
    stack = []

    # 괄호검사 결과
    # 1이면 ok, 0이면 err
    answer = 1

    # 괄호검사
    # check 문자열에서 한글자씩 떼어와서 검사
    for c in check:
        # 문자 하나 떼어온거를 c라고 하자
        # 1. c가 여는 괄호인가?(왼쪽괄호) => 스택 push
        if c == "(":
            stack.append(c)

        # 2. c가 닫는 괄호인가?(오른쪽괄호)
        # 스택이 비어있으면 안된다.
        # 스택이 비어있으면 왼쪽괄호의 수보다 오른쪽 괄호 수가 많다.
        if c ==")":
            if not stack:
                # 스택이 비어있으면 괄호가 잘못되었다
                answer = 0
                break

            # 스택에서 여는괄호를 하나 꺼내서 짝이 맞는지 검사
            left = stack.pop()
            # 괄호의 종류가 다르면 err
            if not (left == "(" and c == ")"):
                answer = 0
                break

        if c == "{":
            stack.append(c)

        # 2. c가 닫는 괄호인가?(오른쪽괄호)
        # 스택이 비어있으면 안된다.
        # 스택이 비어있으면 왼쪽괄호의 수보다 오른쪽 괄호 수가 많다.
        if c =="}":
            if not stack:
                # 스택이 비어있으면 괄호가 잘못되었다
                answer = 0
                break

            # 스택에서 여는괄호를 하나 꺼내서 짝이 맞는지 검사
            left = stack.pop()
            # 괄호의 종류가 다르면 err
            if not (left == "{" and c == "}"):
                answer = 0
                break

        if c == "[":
            stack.append(c)

        # 2. c가 닫는 괄호인가?(오른쪽괄호)
        # 스택이 비어있으면 안된다.
        # 스택이 비어있으면 왼쪽괄호의 수보다 오른쪽 괄호 수가 많다.
        if c =="]":
            if not stack:
                # 스택이 비어있으면 괄호가 잘못되었다
                answer = 0
                break

            # 스택에서 여는괄호를 하나 꺼내서 짝이 맞는지 검사
            left = stack.pop()
            # 괄호의 종류가 다르면 err
            if not (left == "[" and c == "]"):
                answer = 0
                break

        if c == "<":
            stack.append(c)

        # 2. c가 닫는 괄호인가?(오른쪽괄호)
        # 스택이 비어있으면 안된다.
        # 스택이 비어있으면 왼쪽괄호의 수보다 오른쪽 괄호 수가 많다.
        if c ==">":
            if not stack:
                # 스택이 비어있으면 괄호가 잘못되었다
                answer = 0
                break

            # 스택에서 여는괄호를 하나 꺼내서 짝이 맞는지 검사
            left = stack.pop()
            # 괄호의 종류가 다르면 err
            if not (left == "<" and c == ">"):
                answer = 0
                break

    # 문자열 검사 끝난후에 스택이 비어있지 않으면 err
    # 스택 안에 왼쪽괄호가 남아있으면
    # 왼쪽괄호의 수가 오른쪽괄호의 수보다 많다 => err
    if stack:
        answer = 0

    print(f"#{tc} {answer}")