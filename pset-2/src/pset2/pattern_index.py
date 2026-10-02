def patternIndex(text: str, pattern: str) -> list[int]:
    # get indices in the text that are starting points for the pattern
    starts = []
    
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            starts.append(i)

    return starts
