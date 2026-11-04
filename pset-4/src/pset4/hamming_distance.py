def hammingDistance(p, q) :
    ham_dist = 0
    for i in range(len(p)):
        if not p[i] == q[i] :
            ham_dist = ham_dist+1
    return ham_dist
