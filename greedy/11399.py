N = int(input())
list = list(map(int, input().split()))

list.sort()
result = 0

for i in range(0, N) :
    sum = 0
    for j in range(0, i+1) :
        sum += list[j]
    result += sum 

print(result)