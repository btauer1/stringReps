def X_FrequentWords(text, k, x) :
    words = {}
    for i in range(len(text)-k+1) :
        if text[i:(i+k)] in words :
            words[text[i:(i+k)]] = words[text[i:(i+k)]] + 1
        else :
            words[text[i:(i+k)]] = 1
    x_maxwords = []
    for key, value in words.items() :
        if value >= x :
            x_maxwords.append(key)
    return(x_maxwords)

def findClumps(genome, k, L, t) :
    kmers = []
    for j in range(len(genome)-L+1) :
        list_a = X_FrequentWords(genome[j:(j+L)], k, t)
        for x in range(len(list_a)) :
            if list_a[x] not in kmers :
                kmers.append(list_a[x])
    return kmers
