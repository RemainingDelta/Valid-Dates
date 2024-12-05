import math

def r(n):
    if (n == 1):
        return 0
    else:
        return int(math.factorial(n) * math.factorial(n-1) * math.pow(2,n) * math.pow(2,n-1))

def t(n, permutations):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 16
    if n == 3:
        return 384
    for k in range (2,n+1):
        if k == n - 1:
            continue
        permutations = permutations + math.comb(n-1, k-1) * math.comb(n, k) * r(k) * t(n-k, permutations)
    return permutations

n = int(input("How many pairs? "))
#print (r(n))
print(t(n,0))