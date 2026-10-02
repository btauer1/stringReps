def countNucleotides(text: str) -> dict[str, int]:
    
    an = 0
    cn = 0
    gn = 0
    tn = 0

    for i in range(len(text)):
        if text[i] == "A" :
            an = an + 1
        elif text[i] == "C" :
            cn = cn + 1
        elif text[i] == "G" :
            gn = gn + 1
        elif text[i] == "T" :
            tn = tn + 1

    d = {}
    d["A"] = an
    d["C"] = cn
    d["G"] = gn
    d["T"] = tn

    return d
