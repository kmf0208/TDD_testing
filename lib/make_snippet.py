def make_snippet(word):
    new_word = word.split()
    snippet= new_word[:5]
    if len(new_word) > 5:
        new_snippet = ' '.join(snippet) + '...'
        return new_snippet
    else:
        return word
