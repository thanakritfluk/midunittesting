def concat(a, b):
    """
    Concat two string together.
    :raise: TypeError if A or B is not a string.
    """
    if type(a) != str or type(b) != str:
        print("A and B must be strings.")

    return a + b


def remove_duplicate(a):
    """
    Check for duplicate character in string and remove.
    :raise: TypeError if A is not a string.
    """
    if type(a) != str:
        raise TypeError("A must be a string.")

    for index in range(len(a) - 1):
        if a[index] == a[index + 1]:
            a = a[index + 1:]
            a -= 1

    return a


def duplicate(a, round):
    """
    Duplicate string for specified round
    :raise: TypeError if A is not a string, or round is not a number
    """
    return a * round


def find(a, char):
    """
    Find character in string and return index.a
    :raise: TypeError if a or char is not string.
    """
    for i in range(len(a)):
        if a[i] == char:
            return i
