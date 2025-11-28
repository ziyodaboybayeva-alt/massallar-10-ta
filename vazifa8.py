def calculate_product(s):
    if not s.strip():
        return 0

    nums = [int(x) for x in s.split()]
    product = 1

    for num in nums:
        if num == 0:
            return 0
        product *= num

    return product
