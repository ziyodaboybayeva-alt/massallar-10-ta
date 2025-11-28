def fizz_buzz(n):
    out = []
    for i in range(1, n + 1):
        text = ""
        if i % 3 == 0:
            text += "Fizz"
        if i % 5 == 0:
            text += "Buzz"
        out.append(text if text else str(i))
    return out
