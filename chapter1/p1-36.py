def word_count(string):
    words = string.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    print(d)

word_count('I I I I am Janice janice janice kaka kaka ka I lil')
