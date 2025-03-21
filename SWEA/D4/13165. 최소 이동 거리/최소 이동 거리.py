import heapq

testcase = int(input())
for tc in range(1, testcase + 1):
    ans = 0
    n, e = map(int, input().split())
    arr = [[] for _ in range(n + 1)]

    for i in range(e):
        s, e, w = map(int, input().split())
        arr[s].append((e, w))

    result = [21e8] * (n + 1)
    result[0] = 0
    pq = [(0, 0)]  

    while pq:
        price, ky = heapq.heappop(pq)
        if result[ky] < price: continue
        for do, do_cost in arr[ky]:
            if result[do] > price + do_cost:
                result[do] = price + do_cost
                heapq.heappush(pq, (price + do_cost, do))
    ans = result[n]
    print(f'#{tc} {ans}')