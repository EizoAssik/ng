# encoding=utf8
"""
This stuff is inspired by Haskell and designed to model any sequence of computation,
"""


class Monad:
    """
    As Python is quite not a lazy language, modeling sequence of computation
    is not the key-point of `Monads'. Instant, simplifying code does.
    """
    def bind(self, func):
        """
        Just like (>>=) in Haskell.
        """
        return NotImplemented

    def mbind(self, func):
        """
        The more simple version of bind which SHOULD implements the monad's structure
        inside these method. That's the `func' only handles the value, and when func
        fails, mbind is excepted to return a reasonable object.
        """
        return NotImplemented

    def then(self, func):
        """
        Just like return in Haskell's Monads, and not all the Monads has to
        implement it.
        """
        return NotImplemented

    def mreturn(self, value):
        """
        Just like return in Haskell's Monads
        """
        return NotImplemented

    def __str__(self):
        return "{}".format(self.__class__.__name__)


class Maybe(Monad):
    NOTHING = 'Nothing'
    JUST = 'Just'

    def __init__(self, nothing=False, just=None):
        if nothing:
            self.type = Maybe.NOTHING
        else:
            self.type = Maybe.JUST
            self.value = just

    def bind(self, func):
        return func(self)

    def mbind(self, func):
        if self.type is Maybe.JUST:
            try:
                return Maybe(just=func(self.value))
            except:
                return Maybe(nothing=True)
        return Maybe(nothing=True)

    def mreturn(self, value):
        return Maybe(just=value)

    def __str__(self):
        if self.type is Maybe.JUST:
            return "{} {!s}".format(Maybe.JUST, self.value)
        else:
            return Maybe.NOTHING


class MList(Monad):
    def __init__(self):
        self._list = []

    def mreturn(self, value):
        return [value]


def minc(maybe):
    return maybe + 1

def inc(maybe):
    if maybe.type is Maybe.JUST:
        return Maybe(just=maybe.value+1)
    return Maybe(nothing=True)

if __name__ == '__main__':
    f = Maybe(just=233)
    n = Maybe(nothing=True)
    print(f.mbind(minc).mbind(minc).mbind(minc))
    print(n.mbind(minc))
    print(f.bind(inc).bind(inc).bind(inc))
    print(n.bind(inc))
