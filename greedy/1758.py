N = int(input())
list = [0] * N
tip = 0

for i in range(0, N) :
    list[i] = int(input())

list.sort(reverse=True)

for i in range(0, N) :
    if list[i] - i < 0 :
        continue
    else :
        tip += list[i] - i

print(tip)