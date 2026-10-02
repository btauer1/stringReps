"""Find the most frequent words of a given length in text."""

from .pattern_count import PatternCount

def FrequentWords(text: str, k: int) -> set[str]:
    """Return all length-k substrings with the highest occurrence count.

    Count overlapping, case-sensitive matches and include every tie once.
    Assume k is a positive integer. Return an empty set if k exceeds the
    length of text or text is empty.

    Example:
        FrequentWords("ATAT", 2) returns {"AT"}.
        FrequentWords("ATGC", 2) returns {"AT", "TG", "GC"}.

    PatternCount is already imported above. You can call
    PatternCount(text, pattern) directly in your implementation.
    """
    freqPatterns :set[str] = set()
    count :list[int] = []

    # count the frequency of the k-mer starting at each index in the sequence
    for i in range(len(text)-k+1):
        pattern :str = text[i:i+k]
        count.append(PatternCount(text, pattern))

    # find the maximum frequency of k-mers
    maxCount :int = max(count)

    # find all the k-mers that appear with maximum frequency
    for i in range(len(text)-k):
        if count[i] == maxCount:
            freqPatterns.add(text[i:i+k])

    return freqPatterns