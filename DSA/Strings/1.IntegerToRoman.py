def int_to_roman(num):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    roman = []

    for v, s in zip(values, symbols):
        if num == 0:
            break
        while num >= v:
            roman.append(s)
            num -= v

    return "".join(roman)
