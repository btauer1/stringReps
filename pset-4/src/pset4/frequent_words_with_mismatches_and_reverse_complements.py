def hamming(text_a, text_b):
    ham_dist = 0
    for i in range(len(text_a)):
        if not text_a[i] == text_b[i] :
            ham_dist = ham_dist+1
    return ham_dist

def PatternCount_approx(text, pattern, d) :
    count = 0
    for i in range(len(text)-len(pattern)+1) :
        missing = 0
        text_part = text[i:(i+len(pattern))]
        if hamming(text_part, pattern) < d+1 :
            count = count + 1
                
    return count

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

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    nucs = ["A", "C", "G", "T"]
    temp = ["A", "C", "G", "T"]
    temp_2 = []

    while len(temp[1])<k :
        for i in range(len(temp)):
            for j in nucs:
                temp_2.append(temp[i] + j)
        temp = temp_2
        temp_2 = []

    counts = {}
    max = 0

    for i in temp:
        pattern = i
        pattern_rc = reverseComplement(pattern)
        counts[pattern]= PatternCount_approx(text, pattern, d) + PatternCount_approx(text, pattern_rc, d) 
        if counts[pattern] > max:
            max = counts[pattern]

    freqWords = set()
    for p in counts:
        if counts[p] == max:
            freqWords.add(p)
    
    return freqWords
