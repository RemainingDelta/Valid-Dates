import math

def t(n):
    # set T(n) value for n = 0 as 1
    if n == 0:
        return 1
    # set T(n) value for n = 1 as 0
    if n == 1:
        return 0

    # T(n) = 4n * (n-1) * T(n-1) + 16 * nCr(n, 2) * (n-1) * T(n-2)
    permutations = 4 * n * (n-1) * valid_pairs[n-1] + 16 * math.comb(n, 2) * (n-1) * valid_pairs[n-2]

    # return permutations value
    return permutations


# T(n) list set to [] 
valid_pairs = []

# for n: [1-10], find t(n) and add it to valid_pairs list
for n in range(11):
    valid_pairs.append(t(n))

# print valid_pairs
print("T(n):", valid_pairs)
