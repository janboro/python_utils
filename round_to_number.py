import math


def round_to_base(base, x, round_to: int = 1):
    print(math.floor(float(x) / base))
    return round(base * math.floor(float(x) / base), round_to)


lt = {
    "15.0": {"4.0": 1.1, "5.0": 1.1, "6.0": 1.1, "7.0": 1.1},
    "17.5": {"2.0": 1.1, "3.0": 1.1, "7.0": 1.1},
    "20.0": {"2.0": 1.1, "3.0": 1.1, "7.0": 1.1},
    "22.5": {"2.0": 1.1, "3.0": 1.1, "7.0": 1.1},
    "25.0": {"2.0": 1.1, "3.0": 1.1, "4.0": 1.1, "5.0": 1.1, "6.0": 1.1, "7.0": 1.1},
    "27.5": {"5.0": 1.1, "6.0": 1.1, "7.0": 1.1},
}
lt2 = {
    "15.0": 5.0,
}

pp = 13.4
rounded_pp = round_to_base(2.5, pp)

print(rounded_pp)
print("15.0" in lt2)
# print(lt[str(rounded_pp)]["5.0"])
