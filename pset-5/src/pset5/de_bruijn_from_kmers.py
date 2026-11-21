def deBruijnFromKmers(patterns) :

    patterns = sorted(patterns)
    k = len(patterns[0])
    deBruijn = []

    for i in patterns :
        deBruijn.append([i[0:k-1], i[1:k]])

    return(deBruijn)
