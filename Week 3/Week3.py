"""
Practice problems for Python in COMP249/ITEC649

Author: Steve Cassidy
Email: steve.cassidy@mq.edu.au
"""


def longest(string1, string2):
    """Return the longest string from the two arguments,
    if the strings are the same length, return the first string

    >>> longest('this', 'that one')
    'that one'

    >>> longest('this one', 'that')
    'this one'

    >>> longest('this', 'that')
    'this'

    ## Test that the function returns a value (rather than printing)
    >>> longest('this', 'that one') is 'that one'
    True
    """
    leng1=len(string1)
    leng2=len(string2)

    if leng1>leng2:
        return string1
    if leng1<leng2:
        return string2
    else:
        return string1

    if __name__ == "__main__":
        print(longest('this', 'that one'))
        print(longest('this one', 'that'))
        print(longest('this', 'that'))

def count_over(thelist, n):
    """Return the number of integers in thelist that are
    greater than the integer n

    >>> count_over([1,2,4,5,6], 3)
    3
    >>> count_over([5,1,3,5,1], 3)
    2
    >>> count_over([0,0,0,0,0], 3)
    0
    >>> count_over([1,2,4,5,6], 3) == 3
    True
    """

    count = 0
    for list in thelist:
        if list > n:
            count+=1
    return count

if __name__ == "__main__":
    print(count_over([1,2,4,5,6], 3))
    print(count_over([5,1,3,5,1], 3))
    print(count_over([0,0,0,0,0], 3))


def bmi(height, weight):
    """Given a height (m) and weight (kg) (numbers) compute the
    Body Mass Index for an individual.
    Return the BMI as a float

    >>> bmi(1.85, 85)
    24.835646457268076
    >>> bmi(1.44, 56)
    27.006172839506174
    >>> bmi(1, 50)
    50.0
    """

    height = float(height)
    weight = float(weight)
    return weight/(height * height)


if __name__ == "__main__":
    # run the doctests for the functions in this file in verbose mode
    # so that we see output from correct tests
    import doctest
    doctest.testmod(verbose=True)
