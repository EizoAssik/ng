# encoding=utf8


class composition:
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


def foldr(func, iterable):
    return fold(func, reversed(iterable))
