def PatternCount(text, pattern) :
    count = 0
    for i in range(len(text)-len(pattern)+1) :
        if text[i:(i+len(pattern))] == pattern :
            count = count + 1
    return count


def frequencyArray(text, k) :
    nucs = ["A", "C", "G", "T"]
    k_list = []
    num_list = []
    
    temp = ["A", "C", "G", "T"]
    temp_2 = []

    while len(temp[1])<k :
        for i in range(len(temp)):
            for j in nucs:
                temp_2.append(temp[i] + j)
        temp = temp_2
        temp_2 = []

    for i in temp :
        num_list.append(PatternCount(text, i))

    return(num_list)
