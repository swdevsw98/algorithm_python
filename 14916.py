n = int(input())
1
money = [5,2]
result = 0

for i in money:
    if n <= 1 or n == 3 :
        break
    a = n // i #몫
    b = n % i #나머지
    if b % 2 == 0 :
        result += a
        n -= i * a
        continue
    else :
        result += a-1
        n -= i * (a-1)
        continue

if result >= 1 :
    print(result)
else :
    print(-1)
    
