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
    counts = {}
    max = 0

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        pattern_rc = reverseComplement(pattern)
        counts[pattern]= PatternCount_approx(text, pattern, d) + PatternCount_approx(text, pattern_rc, d) 
        if counts[pattern] > max:
            max = counts[pattern]

    freqWords = set()
    for p in counts:
        if counts[p] == max:
            freqWords.add(p)
    
    return freqWords
