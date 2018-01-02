#  Q1
from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        b = -b
    else:
        b = b
    return a + b


# Q2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a * a + b * b, b * b + c * c, c * c + a * a)


# Q3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    k = n - 1
    while 0 < k < n:
        if n % k == 0:
            return k
        else:
            k -= 1


# Q5
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    list_of_hailstone = [
        1,
    ]
    k = n
    while 1 < k:
        list_of_hailstone.append(k)
        print(int(k))
        if k % 2 == 0:
            k = k / 2
        elif k % 2 == 1:
            k = k * 3 + 1
    print(1)
    return len(list_of_hailstone)
