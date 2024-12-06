import math

def r(n):
    # set R(n) value for n = 0 as 1
    if n == 0:
        return 1
    # set R(n) value for n = 1 as 0
    if n == 1:
        return 0
    
    # R(n) = n! * (n-1)! * 2^n * 2^(n-1)
    return int(math.factorial(n) * math.factorial(n - 1) * math.pow(2, n) * math.pow(2, n - 1))

def t(n):
    # set T(n) value for n = 0 as 1
    if n == 0:
        return 1
    # set T(n) value for n = 1 as 0
    if n == 1:
        return 0
    
    # set permutations to 0
    permutations = 0

    # T(n) = sigma k = 2 to n R(k) * nCr(n-1, k-1) * nCr(n, k) * T(n-k) except for when k = n - 1
    for k in range(2, n + 1):
        # if k = n - 1, then skip this iteration 
        if k == n - 1:
            continue
        permutations += r(k) * math.comb(n - 1, k - 1) * math.comb(n, k) * t(n - k)

    # return permutations value
    return permutations

# make t(n) list and prints for n values of 1-10 
def make_t_list():
    # T(n) list set to [] 
    valid_pairs = []

    # for n: [1-10], find t(n) and add it to valid_pairs list
    for n in range(11):
        valid_pairs.append(t(n))

    # print valid_pairs
    print("T(n):", valid_pairs)
    

make_t_list()
