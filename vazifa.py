def reverse_integers(x: int) -> int:
    s = str(x)
    s = s.replace("-", "")   
    s = s.replace("0", "")  
    s = s[::-1]              
    return int(s) if s else 0

assert reverse_integers(123) == 321
assert reverse_integers(-123) == 321
assert reverse_integers(120) == 21
assert reverse_integers(-1050) == 51






