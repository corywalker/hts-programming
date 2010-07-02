import sys

def count_letters(s):
    '''From http://snippets.dzone.com/posts/show/511'''
    return dict((c, s.count(c)) for c in s)

def analyze_list(filename, trim):
    word_list = []
    f = open(filename)
    for line in iter(f):
        word = line[:-trim]
        word_list.append((word, count_letters(word)))
    f.close()
    return word_list

def unscramble_word(scrambled, unscrambled_list):
    for unscrambled in unscrambled_list:
        if unscrambled[1] == scrambled[1]:
            return unscrambled[0]
    return 'None'

unscrambled_list = analyze_list(sys.argv[1], 2)
scrambled_list = analyze_list(sys.argv[2], 1)

unscrambled_words = []
for scrambled in scrambled_list:
    unscrambled_word = unscramble_word(scrambled, unscrambled_list)
    unscrambled_words.append(unscrambled_word)

print ','.join(unscrambled_words)
