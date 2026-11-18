def stringSpelledByGenomePath(patterns) :
    
    n = len(patterns)
    text = ""

    for i in range(n-1) :
        text = text + patterns[i][0]

    text = text + patterns[n-1]

    return(text)
