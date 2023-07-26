n = int(input())
array = list(map(int, input().split()))
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)
    
print(max(d))
# 10 20 10 30 20 50
# 1: 10 -> 1
# 2: 10 < 20 -> 2
# 3: 20 > 10 -> 2
# 4: 10 < 30 -> 3
# 6: 20 < 50 -> 4
