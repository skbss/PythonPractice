n=int(input())
total = 0
num = ''
for i in range(0, n):
    num = ''
    for j in range(0,i+1):
        num+=str(n)
    #print(num)
    total += int(num)
print(total)