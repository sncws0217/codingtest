def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

lines = []
result = 0

for i in range(m):
    a, b, c = map(int, input().split())
    lines.append((c, a, b))

lines.sort()

for line in lines:
    c, a, b = line
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c


print(result)