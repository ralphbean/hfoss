""" This is a module that contains an example of functions in python. """


def hello_world(**unexpanded_kw_args):
    """ This is a function and it's doc-string.  You can reference the text of
    this docstring like this:

        >>> print hello_world.__doc__

    You can even modify it (ridiculously) like:

        >>> hello_world.__doc__ += " (threebean wuz here!)"
        >>> print hello_world.__doc__
    """

    # You gotta be sure
    if not unexpanded_kw_args.get('sure', False):
        return

    # Exciting
    if unexpanded_kw_args.get('yes'):
        unexpanded_kw_args['name'] += '!!!'

    # Down to business
    print "Hello,", unexpanded_kw_args['name']

print "-" * 79
print hello_world.__doc__
print "-" * 79

hello_world.__doc__ += " (threebean wuz here!)"

print hello_world.__doc__
print "-" * 79

some_kw_args = {
    'sure': True,
    'yes': False,
    'name': "William of Old",
}
hello_world(**some_kw_args)
