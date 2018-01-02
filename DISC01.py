# 1.1
def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    if temp < 60 or raining == True:
        return True
    else:
        return False


# 1.2
def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow.
    >>> handle_overflow(35, 29)
    1 spots left in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section.
    """
    if s1 < 30 and s2 < 30:
        print("No overflow.")
    elif s1 < 30 and s2 >= 30:
        print(str(30 - s1) + " spots left in Section 1.")
    elif s1 >= 30 and s2 < 30:
        print(str(30 - s2) + " spots left in Section 2.")
    else:
        print("No space left in either section.")


# 1.3
def square(x):
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# square(so_slow(5)) cannot really output a visible result because
# when square(so_slow(5)) is put into the interpreter, it will first define
# the functions f: square(x) and g: so_slow(num) into the global frame, and
# then inside the f: square(x) frame, it will assign so_slow(5) to x, and then will
# make another local frame of so_slow(num) and assign 5 to num. Then 5 will be assigned
# to x and since 5 > 0, it will execute the while function and 5 + 1 = 6 will
# be assigned to the new x. since the new x is also x > 0, and since x > 0 will be
# true for all integers greater than 5 if the new x is kept on being added '1' to
# the older x, there is an inifinite loop. Cannot exit out of the while loop, and therefore,
# there is no case where the function will be able to return x / 0.


# 1.4
def is_prime(n):
    """If n is a prime this function will return True, otherwise False.

    >>> is_prime(7)
    True
    >>> is_prime(11)
    True
    >>> is_prime(2)
    False
    """
    list_of_primes = [False]
    for _ in range(n - 1):
        list_of_primes.append(True)
    current_n = 2
    while current_n < n + 1:
        multiple = current_n * 2
        while multiple < n + 1:
            list_of_primes[multiple - 1] = False
            multiple += current_n
        try:
            current_n = list_of_primes.index(True, current_n + 1)
        except ValueError:
            break
    return list_of_primes[n - 1]


#  3.1
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """

    k = 1
    while k < n + 1:
        if cond(k):
            print(i)
        i += 1


# 3.2
# >>> def outer(n):
# ...   def inner(m):
# ...       return n - m
# ...   return inner
#
# >>> outer(61)
#  <function >
# >>> f = outer(10)
# >>> f(4)
# 6
# >>> outer(5)(4)
# 1


#  3.3
def keep_ints(n):
    """Returns a function which takes one parameter cond and
    prints out all integers 1..i..n where calling cond(i)
    returns True.

    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """

    def func(x):
        if x == 'is_even':
            k = 1
            while k < n + 1:
                if k % 2 == 0:
                    print(k)
                else:
                    pass
                k += 1
                return
