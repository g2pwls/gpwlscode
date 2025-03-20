T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T+1):
    # N: 학생 수
    # K: 학점을 알고싶은 학생의 번호
    N, K = map(int, input().split())
    # score = 총점, 학생번호를 저장할 빈 리스트
    scores = []

    # 학생들의 총점을 알기 위해 계산 반복문
    for i in range(N):
        score = list(map(int, input().split()))
        total_score = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
        scores.append((total_score, i+1)) # (총점, 학생번호) 저장

    # 학생들의 점수를 내림차순 정렬
    # key=lambda x: x[0] 튜플의 첫 번째 값(총점) 기준으로 정렬
    scores.sort(reverse=True)

    # 학점 부여 (같은 비율로 나눔)
    num_grade = N // 10  # 한 학점당 부여할 학생 수
    # 학생번호를 Key, 학점을 Value로 저장하는 빈 딕셔너리
    grade_dict = {}

    for i in range(N):
        # scores는 (총점, 학생번호)
        # scores[i] : i번째 학생의 (총점, 학생번호)
        # scores[i][1]: i번째 학생의 학생번호

        # grades 리스트에 학점이 들어있음
        # i // num_grade: 현재 학생이 몇 번째 학점 그룹인지
        grade_dict[scores[i][1]] = grades[i // num_grade]

    print(f"#{tc} {grade_dict[K]}")