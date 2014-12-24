#! python

import functools

"""Create the function described in the docstring below--essentially, a
   decorator that takes an argument.  Import it into a module I can run to
   see if the code works.
"""

def minimum_x(min_x):
    """Higher-level decorator that will return another decorator that
       validates the first argument of a function: if that value is less
       than `min_x`, raise a ValueError.
    """
    def _min_fn(fn):
        """Decorator that returns wrapped version of function. Will enforce
           the value of the first argument and make sure it's at least the
           value of `min_x`.
        """
        # Use .wraps to carry along docstring and some of the original matadata
        @functools.wraps(fn)
        def _wrapped_fn(x, *args, **kwargs):
            if x < min_x:
                raise ValueError(x)
            return fn(x, *args, **kwargs)
        return _wrapped_fn
    return _min_fn

