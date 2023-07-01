n = int(input())

list = []
for _ in range(n) :
    a, b = map(int, input().split())
    list.append([a,b])

s = 0
for i in list :
    s += i[1]

s /= 2

list.sort(key = lambda x : x[0])

ss = 0
for i in range(n):
    ss += list[i][1]
    if ss >= s :
        print(list[i][0])
        break
    


