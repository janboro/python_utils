def float_equal(x: float, y: float, precision: float = 0.0001) -> bool:
    return abs(x - y) <= precision
