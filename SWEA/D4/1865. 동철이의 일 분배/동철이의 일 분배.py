# DFS: 깊이 우선 탐색: 모든 경우를 탐색
# 백트래킹: 현재 확률이 최댓값보다 작아지면 더 탐색하지 않고 중단
# level: 현재 배정한 직원 수 (몇번째 직원까지 일을 배정했는지)
# gop: 현재까지 계산한 성공 확률의 곱 (선택된 직원들의 확률을 곱한 값)
def dfs(level, gop):
    global Max
    # 현재까지 구한 성공 확률(gop)이 최대값(max)보다 작다면 더 탐색 x (백트래킹)
    if Max >= gop: return   # backtracking 요소 추가
    # 만약 모든 직원이 일을 배정받았으면
    if level == N:
        # 현재까지 구한 성공 확률(gop)을 max와 비교해서 최대값 갱신
        Max = max(Max, gop)
        return

    # 현재 직원에게 모든 일 중 하나를 배정하는 경우
    for i in range(N):
        # 다른 직원이 맡은 일이면 건너뜀
        # 1이면 이미 배정한 일 0이면 배정 안한 일
        if used[i] == 1:
            continue
        # 배정 받지 않은 일이라면
        # 배정 받았다고 표시하고
        used[i] = 1
        # 다음 직원으로 이동,
        # 현재까지 확률에 지금 선택한 확률을 곱함
        dfs(level+1, gop*(lst[level][i]/100))
        # 탐색 끝나면 원래 상태로 되돌림 (백트래킹)
        used[i] = 0

T = int(input())

for tc in range(1, T+1):
    # 주어진 일이 모두 성공할 확률의 최댓값
    ans = 0
    # N: 직원수, 할일 수
    N = int(input())
    # N줄 만큼 반복할 것, 리스트로 받는다.
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 각 일을 배정 받았는지 여부를 저장하는 리스트
    used = [0]*N
    # 최대값을 저장하는 변수, 아주 작은 값으로 초기화
    Max =- 21e8   # -21 곱하기 10의 8승 지수표기법
    # level 0부터 시작: 첫번째 직원부터 탐색, 확률 1 (100%)
    dfs(0, 1)   # level gop
    # 최대값을 퍼센트 단위로 변환
    ans = Max*100
    # 소숫점 6자리까지 출력
    print(f'#{tc} {ans:.6f}')