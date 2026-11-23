def stringComposition(k, text) :
    
    Composition = []
    for i in range(len(text)-k+1):
    	Composition.append(text[i:(i+k)])

    Composition = sorted(Composition)
    return(Composition)

def deBruijnFromString(k, text) :

    compostion = stringComposition(k, text)
    deBruijn = []

    for i in compostion :
        deBruijn.append([i[0:k-1], i[1:k]])

    return(deBruijn)
