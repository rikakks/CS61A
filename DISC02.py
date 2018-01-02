#  2.1
def multiply(m, n):
    """This function should return the product of m multiplied by n, without the usage of the
    multiplication function.

    >>> multiply(2, 6)
    12
    >>> multiply(12, 1)
    12
    >>> multiply(3, 4)
    12
    """
    k = 1
    sum = 0
    while k < n + 1:
        sum += m
        k += 1
    return sum


def multiplyy(m, n):
    """This function should return the product of m multiplied by n, without the usage of the
    multiplication function.

    >>> multiplyy(2, 6)
    12
    >>> multiplyy(12, 1)
    12
    >>> multiplyy(3, 4)
    12
    """
    if n == 1:
        return m
    else:
        return m + multiplyy(m, n - 1)


# I would prefer calling multiplyy(m, n- 1) because I've defined function
# so that it will see m as a constant and n as the changing variable.


# 2.2
def countdown(n):
    """This function will print out all the numbers from n to 1 in order.
    >>> countdown(3)
    3
    2
    1
    """
    if n < 1:
        return
    print(n)
    countdown(n - 1)


# 2.3
def countup(n):
    """This function will print out all the numbers from 1 to n in order.
    >>> countup(3)
    1
    2
    3
    """
    if n < 1:
        return
    countup(n - 1)
    print(n)


# 2.4
def sum_digits(n):
    """This function will return the sum of the digits of a number n, where n
    is a positive integer.

    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


#  3.1
def count_stair_ways(n):
    """This function will return the number of ways a stair of n steps can be climbed.

    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    """
    if n < 1:
        return
    elif n == 1 or n == 2:
        return n
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


# 3.2
def count_k(n, k):
    """This function will return the number of ways to climb a stair case of
    n steps when up to k steps could be climed at once.

    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        i = 1
        sum = 0
        while i < k + 1:
            sum += count_k(n - i, k)
            i += 1
        return sum
