class Vegetable(object):
    def __init__(self, *args, **kwargs):
        self.tasty = False

    def __getattr__(self, key):
        return "asking for " + key

    def fibrous(self):
        """ Kale is fibrous, but not tasty. """
        return not self.tasty


if __name__ == '__main__':
    t = Vegetable()

    for attribute in ['tasty', 'color', 'fibrous']:
        thing = getattr(t, attribute)
        if callable(thing):
            print attribute, "is callable.  Calling it."
            thing = thing()
        else:
            print attribute, "is not callable"

        print " *", thing
