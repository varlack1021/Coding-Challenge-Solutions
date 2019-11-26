def comp(array1, array2):
    if None in (array1, array2):
        return False
    return sorted(num ** 2 for num in array1) == sorted(array2)