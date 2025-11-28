def even_chars(s):
    indices = [i for i in range(0, len(s), 2)]
    return "".join(s[i] for i in indices)
