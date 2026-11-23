def transcribeRNA(text) :
    text_rna = ""

    for i in range(len(text)) :
        if text[i] == "T" :
            text_rna = text_rna + "U"
        else :
            text_rna = text_rna + text[i]

    return(text_rna)
