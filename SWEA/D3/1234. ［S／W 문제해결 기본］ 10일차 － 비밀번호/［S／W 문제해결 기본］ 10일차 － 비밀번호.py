T = 10

for tc in range(1, T + 1):
    n, check = input().split()  # 검사할 문자열
    n = int(n) # n을 정수로 변환하는 코드
    s = []  # 사용할 스택
    top = -1  # top을 -1부터 시작 (스택이 비었음을 의미)

    for c in check:
        if top >= 0 and s[top] == c:  # 스택이 비어있지 않고, top 위치의 문자와 같다면 pop
            s.pop()
            top -= 1  # pop 했으므로 top 감소
        else:
            s.append(c)
            top += 1  # push 했으므로 top 증가

    print(f"#{tc} {''.join(s)}")