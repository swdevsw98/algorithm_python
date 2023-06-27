N = int(input())
all = [0] * N

for i in range(0, N) :
    all[i] = int(input())

all.sort(reverse=True)

max = 0
len = 0
for i in all :
    len += 1
    if len == 1 :
        max = i
    else :
        if max < len * i :
            max = len * i

print(max)