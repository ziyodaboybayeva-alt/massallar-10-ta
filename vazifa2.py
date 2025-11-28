def plus_one(digits):
    num = int("".join(map(str, digits)))
    num += 1
    return list(map(int, str(num)))


assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9]) == [1,0]
