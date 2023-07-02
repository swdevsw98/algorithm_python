from collections import deque
n, k = map(int, input().split())

list = [i+1 for i in range(n)]

ans = []
num = 0

for i in range(n):
    num += k-1
    if num >= len(list) :
        num = num % len(list)
    
    ans.append(list.pop(num))

print(str(ans).replace('[' , '<').replace(']', '>'))