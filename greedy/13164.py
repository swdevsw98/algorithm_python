n, k = map(int, input().split())

list = list(map(int, input().split()))

a = []

for i in range(0, len(list)-1) :
    t = list[i+1] - list[i]
    a.append(t)

a.sort()

s = 0
for i in range(0, len(a) - (k-1)) :
    s += a[i]

print(s)
