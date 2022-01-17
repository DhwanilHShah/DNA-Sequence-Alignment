def alignment(
    X, 
    Y, 
    m, 
    n,
    mismatch,
    gap
    ):
    '''
    Function to calculate the optimal alignment for two strings using 2D DP.
    Stores the entire 2D OPT array in the memory

    Arg(s):
        X(str): String 1
        Y(str): String 2
        m(int): Length of string 1
        n(int): Length of string 2
        mismatch(dict): Mismatch costs for letter pairs
        gap(int): Gap cost in alignment
    Output(s):
        align1(str): Aligned string 1
        align2(str): Aligned string 2
    '''

    opt = [
        [j * gap for j in range(n + 1)] if i == 0 
        else [i * gap if j == 0 else 0 for j in range(n + 1)] 
        for i in range(m + 1)]

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            opt[i][j] = min(
                opt[i - 1][j - 1] + mismatch[X[i - 1] + Y[j - 1]], 
                opt[i - 1][j] + gap, 
                opt[i][j - 1] + gap
                )

    align1 = []
    align2 = []
    j = n
    i = m
    while j > 0 and i > 0:
        if opt[i][j] == opt[i - 1][j - 1] + mismatch[X[i - 1] + Y[j - 1]]:
            align1.append(X[i - 1])
            align2.append(Y[j - 1])
            j -= 1
            i -= 1

        elif opt[i][j] == opt[i][j - 1] + gap:
            align1.append('_')
            align2.append(Y[j - 1])
            j -= 1

        elif opt[i][j] == opt[i - 1][j] + gap:
            align1.append(X[i - 1])
            align2.append('_')
            i -= 1

        else:
            print('Error')
            exit()

    while i > 0:
        align1.append(X[i - 1])
        align2.append('_')
        i -= 1
    while j > 0:
        align1.append('_')
        align2.append(Y[j - 1])
        j -= 1

    align1.reverse()
    align2.reverse()
    return "".join(align1), "".join(align2), opt[m][n]