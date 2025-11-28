def tri_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base va height manfiy bo‘lishi mumkin emas.")
    return (base * height) / 2.0
