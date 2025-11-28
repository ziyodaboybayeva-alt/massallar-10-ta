def count_unique_values(s):
    if not s.strip():
        return 0

    uniq = set()
    for x in s.split():
        uniq.add(int(x))
    return len(uniq)
