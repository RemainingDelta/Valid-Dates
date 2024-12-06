import math

def t(n):
    # set T(n) value for n = 0 as 1
    if n == 0:
        return 1
    # set T(n) value for n = 1 as 0
    if n == 1:
        return 0
    
    # set permutations to 0
    permutations = 0

    # T(n) = 4n * (n-1) * T(n-1) + 16 * nCr(n, 2) * (n-1) * T(n-2)
    permutations += 4 * n * (n-1) * t(n-1) + 16 * math.comb(n, 2) * (n-1) * t(n-2)

    # return permutations value
    return permutations

# set n to input value of the number of pairs 
n = int(input("How many pairs? "))

# print T(n)
print("T(n):", t(n))
