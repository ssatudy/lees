table = [[0]*100 for _ in range(100)]

for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            table[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        result += table[i][j]

print(result)