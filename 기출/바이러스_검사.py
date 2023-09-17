n = int(input()) # 식당 수
store = list(map(int, input().split()))
a, b = map(int, input().split())
answer = 0

for s in store:
    if s - a <= 0:
        answer += 1
        continue
    s -= a 
    answer += 1
    answer += s // b
    if s % b != 0:
        answer += 1


print(answer)