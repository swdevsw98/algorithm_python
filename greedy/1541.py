str = input().split("-")
s = 0

for i in str[0].split("+") :
    s += int(i)

for i in str[1:]:
    for j in i.split("+"):
        s -= int(j)

print(s)