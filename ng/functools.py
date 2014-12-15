# encoding=utf8
from functools import reduce as _reduce
from functools import partial as _partial


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


class partial:
    def __init__(self, func, *args, position=None, **kwargs):
        if position and args:
            raise ValueError("Cannot use specified position arguments"
                             + " with non-specified position arguments"
                             + " at same time.")
        if position:
            self._position = position
            self._func = func
        else:
            self._position = False
            self._func = _partial(func, *args, **kwargs)
        self._kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if self._position:
            iargs = iter(args)
            mixed_args = []
            for i in range(len(args) + len(self._position)):
                if i in self._position:
                    mixed_args.append(self._position[i])
                else:
                    mixed_args.append(next(iargs))
            mixed_kwargs = dict(self._kwargs)
            mixed_kwargs.update(kwargs)
            return self._func(*mixed_args, **mixed_kwargs)
        else:
            return self._func(*args, **kwargs)



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
