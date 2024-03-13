def word_occ(n, words):
    word_count = {}
    distinct_words = []
    occurrences = []

    for word in words:
        if word not in word_count:
            word_count[word] = 1
            distinct_words.append(word)
        else:
            word_count[word] += 1

    for distinct_word in distinct_words:
        occurrences.append(str(word_count[distinct_word]))

    return len(distinct_words), ' '.join(occurrences)

#