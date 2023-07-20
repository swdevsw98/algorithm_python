N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())
    

max = 0
stack = []
res = []
for i in arr:
    if max < i:
        while max < i:
            max += 1
            stack.append(max)
            res.append('+')
    
    if stack[-1] == i:
        stack.pop()
        res.append('-')
    else :
        res.append('-1')
        break



if "-1" in res :
    print("NO")
else :
    for i in res :
        print(i)

