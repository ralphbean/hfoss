""" This is the module level docstring. """

import inspect
import sys


def my_doc(n=1):
    """ Print the docstring of the calling function """
    frame = inspect.stack()[n][0]
    return frame.f_globals[frame.f_code.co_name].__doc__


def f(x=None):
    """ This is function f.  It has a docstring.

    It is many lines long, and might provide examples.
    """

    # Validate the input
    if x == None:
        print my_doc()
        print "You must provide a value for 'x'."
        return ""

    # Otherwise, do the work we intended to do.
    return "%r is your value!" % x


if __name__ == '__main__':
    print __doc__   # Print the module level docstring
    print "-" * 50  # Separate our output
    print "About to run function f:"
    print inspect.getsource(f)
    print "-" * 50  # Separate our output
    print f()       # Run it with a broken input.
    print "-" * 50  # Separate our output
    print f('foo')  # Run it with good input.
