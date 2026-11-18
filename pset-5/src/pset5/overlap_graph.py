def overlapGraph(patterns) :
    adjacent = []
    k = len(patterns[0])

    for i in range(len(patterns)) :
        for j in range(len(patterns)) :
            if patterns[i][1:k] == patterns[j][0:k-1] :
                adjacent.append([i,j])

    return(adjacent)
