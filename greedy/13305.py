N = int(input())
cityLen = list(map(int, input().split()))
cityPrice = list(map(int, input().split()))

result = 0

for i in range(0, N-1) :
    if i == 0 :
        minPrice = cityPrice[i]
        result += minPrice * cityLen[i]
    else :
        price = cityPrice[i]
        if minPrice >= price :
            minPrice = price
        result += minPrice * cityLen[i]
    

    
print(result)
    
        
    
