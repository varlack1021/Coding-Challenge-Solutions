def rotLeft(a, d):
    first_half = a[d:]
    second_half =a[:d]
    first_half.extend(second_half)