n = int(input())
list = []

for _ in range(n) :
    start, end= map(int,input().split())
    tup = (start, end)
    list.append(tup)

t1 = sorted(list, key=lambda x:x[1])

for i in range (0, n-1) :
    if t1[i][1] == t1[i+1][1] :
        if t1[i][0] > t1[i+1][0] :
            t = t1[i]
            t1[i] = t1[i+1]
            t1[i+1] = t

print(t1)

c = 0
s = 0
for i in range(0, n) :
    if i == 0:
        s = t1[i][1]
        c += 1
        continue
    if s <= t1[i][0] :
        s = t1[i][1]
        c += 1

print(c)
            