# encoding=utf8
"""
The idea from Haskell
"""


class FMapObject:
    """
    This only provide the fmap protocol to target objects.
    You can always just add __fmap__ method to you classes
    on your own without even knowing this.
    """
    def __fmap__(self, func, force_lazy=True):
        return NotImplemented


def fmap(func, target, force_lazy=False):
    if isinstance(target, FMapObject) or hasattr(target, "__fmap__"):
        return target.__fmap__(func, force_lazy=force_lazy)
    else:
        # when given a iterable instant of a FMapObject
        try:
            m = map(lambda x: fmap(func, x, force_lazy=force_lazy), target)
            # this may cause
            if force_lazy:
                return m
            else:
                constructor = type(target)
                return constructor(m)
        except:
            raise NotImplementedError("This object has not implemented fmap protocol.")

