T = int(input())

for tc in range(1, T+1):
    temp, N = (input().split())
    str1 = (input().split())
    result = [0] * int(N)
    result2 = [""] * int(N)
    list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    for i in range(len(str1)):
        result[i] = dict[str1[i]]
    result.sort()

    for j in range(len(result)):
        result2[j] = list[result[j]]
    print(f"#{tc} \n{' '.join(result2)}")