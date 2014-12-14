# encoding=utf8
from functools import reduce as _reduce


class composition:
    """
    works like DOT (.) in Haskell
    """
    def __init__(self, *args):
        if len(args) < 1:
            raise ValueError(
                "Composition needs at least 2 callables, "
                "{.__len__()} given".format(args))
        self._first = args[-1]
        self._functions = tuple(reversed(args[:-1]))

    def __call__(self, *args, **kwargs):
        v = self._first(*args, **kwargs)
        for fn in self._functions:
            v = fn(v)
        return v


fold = _reduce
# This works, but reduce is implemented in C.
"""
def fold(func, iterabel):
    fold_iter = iter(iterabel)
    try:
        m = next(fold_iter)
    except StopIteration:
        return []
    try:
        n = next(fold_iter)
    except StopIteration:
        return [m]
    result = func(m, n)
    for value in fold_iter:
        result = func(result, value)
    return result
"""


def foldr(func, iterable):
    """
    Fork of foldr1 in Haskell
    """
    return fold(func, reversed(iterable))


def zipWith(func, *args):
    """
    Fork of zipWith in Haskell, returns a map object
    """
    return map(lambda x: func(*x), zip(*args))


def curry(func, *args):
    return func(args)


def uncurry(func, args):
    return func(*args)
