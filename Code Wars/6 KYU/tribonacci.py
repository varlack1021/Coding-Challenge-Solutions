def tribonacci(signature, n):
    if n == 0:
        return []
    while len(signature) != n and n > 3:
        last_three_digits = signature[len(signature)-3::]
        summ = sum(last_three_digits)
        signature.append(summ)
    return signature[0:n]