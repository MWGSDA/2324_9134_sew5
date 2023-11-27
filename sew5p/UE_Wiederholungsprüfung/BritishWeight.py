import functools
import doctest


@functools.total_ordering
class BritishWeight:
    """
    Klasse für britische Gewichter
    """

    def __init__(self, pounds=0):
        if pounds < 0:
            raise ArithmeticError("Ein Gewicht kann nicht negativ sein")
        self._pounds = pounds

    def __str__(self):
        stones = self._pounds // 14
        pounds = self._pounds % 14
        return f"{stones} st {pounds} lb"

    def __repr__(self):
        return f"BritishWeight({self._pounds})"

    def __add__(self, other):
        if isinstance(other, BritishWeight):
            pounds = self._pounds + other._pounds
            return BritishWeight(pounds)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BritishWeight):
            return self._pounds == other._pounds
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BritishWeight):
            return self._pounds < other._pounds
        return NotImplemented

    @property
    def pounds(self):
        return self._pounds


    def run_tests(self):
        """
        >>> w1 = BritishWeight(13)
        >>> w2 = BritishWeight(1)
        >>> w3 = BritishWeight(-5)
        Traceback (most recent call last):
            ...
        ArithmeticError: Ein Gewicht kann nicht negativ sein
        >>> print(w1)
        0 st 13 lb
        >>> print(w2)
        0 st 1 lb
        >>> repr(w1)
        'BritishWeight(13)'
        >>> repr(w2)
        'BritishWeight(1)'
        >>> print(w1+w2)
        1 st 0 lb
        """
        doctest.testmod()


    if __name__ == '__main__':
        run_tests()
