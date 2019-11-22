#!/usr/bin/python3

# find all bin strs of length 2n+1
# start indexing at 0
# no more than 3 consecutive 1s
# has exactly k 1s
# runs of 3 must start on an odd index

# any run of R 1s does not begin and
#   end on index cong 0 mod (R-1)
# No runs of length gt 2*R - 3
#   There are 2*r - 1 vertices in a pair
#   of hyperedges, and we don't want either
#   of the two end points either, so 2*r-3


from itertools import *

def getStrings(r : int, n : int):
    """
    Args:
        r: number of vertices in a hyperedge
        n: number of hyperedges
    """
    # there are n length r hyperedges, and all of them overlap w/ the next, except for the last one
    leng = (r * n) - (n - 1) 
    combinations = product([0,1], repeat=leng)

    for combin in combinations:
        i_in_row = 0
        bad = False
        start_index = 0
        index = 0
        for element in combin:
            if element == 1:
                if i_in_row == 0:
                    start_index = index

                i_in_row += 1
            elif element == 0:
                i_in_row = 0
            
            if (i_in_row >= r and index % (r-1) == 0) or i_in_row > 2*r - 3:
                bad = True
                print(f"comb is bad: {combin}")
                break

            index += 1

        if not bad:
            yield combin



if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3: 
        print(f"USAGE: {sys.argv[0]} <r> <n>")
        sys.exit(1)

    count = 0
    r = int(sys.argv[1]) 
    n = int(sys.argv[2])
    for string in getStrings(r, n):
        count += 1

    print(f"F(r={r}, n={n}) = {count}")
