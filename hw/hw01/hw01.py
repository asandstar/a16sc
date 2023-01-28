from operator import add, sub

"""Q2:A Plus Abs B
Fill in the blanks in the following function for adding a to the absolute value of b, without calling abs. 
You may not modify any of the provided code other than the two blanks."""

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

"""Q3: Two of Three
Write a function that takes three positive numbers as arguments 
and returns the sum of the squares of the two smallest numbers. 
Use only a single line for the body of the function.

Hint: Consider using the max or min function:

>>> max(1, 2, 3)
3
>>> min(-1, -2, -3)
-3

"""


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return x * x + y * y + z * z - max(x, y, z) * max(x, y, z)

"""Q4: Largest Factor
Write a function that takes an integer n 
that is greater than 1 and returns the largest integer 
that is smaller than n and evenly divides n.

Hint: To check if b evenly divides a, 
you can use the expression a % b == 0, 
which can be read as, "the remainder of dividing a by b is 0."
"""
  
  
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    for i in range(1, n):
        if n % (n-i) == 0:
            return n-i
        else:
            continue

"""Q5: If Function vs Statement
Let's try to write a function that does the same thing as an if statement.

Despite the doctests above, 
this function actually does not do the same thing as an if statement in all cases. 
To prove this fact, write functions cond, 
true_func, and false_func such that with_if_statement prints the number 47, 
but with_if_function prints both 42 and 47.

说实话其实我不太懂这道题，但是能通过本地ok测试
我用的命令
python ok -q XXXX(function name) --local
"""


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


def cond():
    "*** YOUR CODE HERE ***"
    return False


def true_func():
    "*** YOUR CODE HERE ***"
    print(42)


def false_func():
    "*** YOUR CODE HERE ***"
    print(47)


"""Q6: Hailstone
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

Pick a positive integer n as the start.
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Continue this process until n is 1.
The number n will travel up and down but eventually end at 1
(at least for all numbers that have ever been tried -- 
nobody has ever proved that the sequence will terminate). 
Analogously, a hailstone travels up and down 
in the atmosphere before eventually landing on earth."""
    
    
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
    "*** YOUR CODE HERE ***"

    count = 1

    while (n != 1):
        if (n % 2 == 0):
            print(int(n))
            n = n / 2

        elif (n % 2 != 0):
            print(int(n))
            n = n * 3 + 1
        count += 1
    print(1)
    return count
