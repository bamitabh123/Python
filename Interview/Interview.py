test_str = 'it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness'


def wordcnt(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(wordcnt(test_str))
