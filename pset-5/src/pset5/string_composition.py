def stringComposition(k, text) :
    
    Composition = []
    for i in range(len(text)-k+1):
    	Composition.append(text[i:(i+k)])

    Composition = sorted(Composition)
    return(Composition)
