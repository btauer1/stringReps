from frequent_words import FrequentWords as inclass_frequent_words


def frequentWords(text: str, k: int) -> set[str]:

    # for all indices that begin k-mers,
        # either add 1 to freq for k-mer in dict
        # or create entry for k-mer in dict if it wasn't already in dict
    # and find max count value in dictionary
    counts = {}
    max = 0

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern in counts:
            counts[pattern] += 1
        else:
            counts[pattern] = 1
        if counts[pattern] > max:
            max = counts[pattern]

    # find all the k-mers that appear with maximum frequency
    freqWords = set()
    for p in counts:
        if counts[p] == max:
            freqWords.add(p)
    
    return freqWords
