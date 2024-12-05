from itertools import permutations
import math

# make the sister lists [1, -1, 2, -2, ... , n, -n] 
def make_sibling_lists(n):
    for i in range(0, 2 * n, 2): 
        sisters_list[i] = math.ceil((i + 1)/2)
    for i in range(1, 2 * n, 2): 
        sisters_list[i] = -(math.ceil((i + 1)/2))

# returns the number of valid permutations
def find_valid_perms():
    
    # set count of valid permutations to 0
    count = 0
   
    # generates permutations for sisters_list
    perms = permutations(sisters_list)
    # for each perm in perms, add 1 to count if the perm is valid 
    for perm in perms:
        # set is_valid to True, which assumes from the beginning that every perm is valid
        is_valid = True
        
        # for each even index check if the next index is the negative of the current index to indicate that the permutation is invalid
        for i in range(0, 2 * n, 2): 
            if (perm[i] == -(perm[i+1])):
                is_valid = False
        
        # the permutation is still valid, then add one to the count
        if (is_valid):
            count += 1
    
    # return count at the end with the total valid number of permutations for n pairs
    return count


# set n to input value of the number of pairs 
n = int (input ("How many pairs? "))

# set sisters_list as list of 0s of size 2n
sisters_list = [0] * 2 * n

# make the sister lists 
make_sibling_lists(n)

# print the number of valid date permutations 
print("Valid Dates:", find_valid_perms())
