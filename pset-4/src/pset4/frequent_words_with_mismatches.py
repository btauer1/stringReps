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

def frequentWordsWithMismatches(text, k, d) :
    counts = {}
    max = 0

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        counts[pattern]= PatternCount_approx(text, pattern, d)
        if counts[pattern] > max:
            max = counts[pattern]

    freqWords = set()
    for p in counts:
        if counts[p] == max:
            freqWords.add(p)
    
    return freqWords
