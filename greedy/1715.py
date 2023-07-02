import heapq

n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else :
    ans = 0
    while len(card) > 1 :
        t = heapq.heappop(card)
        t2 = heapq.heappop(card)
        ans += t + t2
        heapq.heappush(card, t + t2)
    print(ans)