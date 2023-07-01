N = int(input())

list = list(map(int, input().split()))

list.sort()

max = list[N-1]
for i in range(0, N-1) :
    if list[i] <= max :
        max += list[i]/2
    else :
        max = list[i] + max/2

print(max)