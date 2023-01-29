def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    sum = n
    if k != 0:
        for i in range(1, k):
            sum = sum * (n-i)
        return sum
    else:
        return 1


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    if y < 10:
        return y
    else:
        all_but_last, last = y // 10, y % 10
        return sum_digits(all_but_last) + last


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    if n < 10:
        return False
    else:
        all_but_last = n
        for i in range(1, len(str(n))):
            all_but_last, last = all_but_last // 10, all_but_last % 10
            if last == 8:
                if all_but_last % 10 == 8:
                    return True
                else:
                    return False
            else:
                continue
        return False
