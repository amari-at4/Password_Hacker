def letters(word):
    index = 0
    while index < len(word):
        yield word[index]
        index += 1
