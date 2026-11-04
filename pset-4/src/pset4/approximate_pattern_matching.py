
def hamming(text_a, text_b):
    ham_dist = 0
    for i in range(len(text_a)):
        if not text_a[i] == text_b[i] :
            ham_dist = ham_dist+1
    return ham_dist

def approximatePatternMatching(pattern, text, d) :
    count = 0
    index = []
    for i in range(len(text)-len(pattern)+1) :
        missing = 0
        text_part = text[i:(i+len(pattern))]
        if hamming(text_part, pattern) < d+1 :
            #count = count + 1
            index.append(i)
                
    return index
