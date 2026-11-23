def reverseComplement(text) :
    text_rc = ""

    for i in range(len(text)) :
        if text[-i-1] == "A" :
            text_rc = text_rc + "T"
        elif text[-i-1] == "C" :
            text_rc = text_rc + "G"
        elif text[-i-1] == "G" :
            text_rc = text_rc + "C"
        elif text[-i-1] == "T" :
            text_rc = text_rc + "A"

    return(text_rc)
    
