def fac(n): # n!
    if(n > 1):
        return n * fac(n - 1)
    else:
        return 1
    
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    mCn = int( fac(m) // ((fac(m - n)) * fac(n)) ) # nCr = n! / (n-r)!r!
    print(mCn)

