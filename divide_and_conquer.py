import math
from alignment import alignment

def divide(X, Y, mismatch_cost, gap_cost):
    m = len(X)
    n = len(Y)
    opt = [[],[]]
    opt[0] = [gap_cost*j for j in range(n+1)]
    for i in range(1,m+1):
        opt[1] = [0 for j in range(n+1)]
        opt[1][0] = i*gap_cost
        for j in range(1,n+1):
            opt[1][j] = min(
                opt[0][j-1] + mismatch_cost[X[i-1]+Y[j-1]], 
                opt[0][j] + gap_cost, 
                opt[1][j-1] + gap_cost
                )

        opt[0] = opt[1]

    return opt[1]

def divide_conquer(X, Y, mismatch_cost, gap_cost):
    m = len(X)
    n = len(Y)

    if m <= 2 or n <= 2:
        return alignment(X, Y, m, n, mismatch_cost, gap_cost)

    col1 = divide(X[:m//2], Y, mismatch_cost, gap_cost)
    col2 = divide(X[:m//2-1:-1], Y[::-1], mismatch_cost, gap_cost)

    minimum = math.inf
    k = -1
    for j in range(n+1):
        if minimum > (col1[j] + col2[n-j]):
            minimum = col1[j] + col2[n-j]
            k = j

    align1, align2, cost1 = divide_conquer(
        X[:m//2], Y[:k], mismatch_cost, gap_cost
        )
    align3, align4, cost2 = divide_conquer(
        X[m//2:], Y[k:], mismatch_cost, gap_cost
        )

    return align1 + align3, align2 + align4, cost1 + cost2
