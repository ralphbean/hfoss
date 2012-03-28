from random import random

class GrandParent(object):
    def awesome(self):
        print "I'm the grandparent."

class Parent1(GrandParent):
    def awesome(self):
        print "I'm parent1"
        super(Parent1, self).awesome()

class Parent2(GrandParent):
    def awesome(self):
        print "I'm parent2"
        super(Parent2, self).awesome()

class Parent3(GrandParent):
    def awesome(self):
        print "I'm parent3"
        super(Parent3, self).awesome()

class SwitchboardMeta(type):
    def __new__(meta, name, bases, dct):
        if bases[-1] == object:
            bases = bases[:-1]

        bases += pick_random_parents()

        if not bases:
            bases = (object,)

        return type.__new__(meta, name, bases, dct)


def pick_random_parents():
    return tuple((p for p in [Parent1, Parent2, Parent3] if random() < 0.5))

class Child(object):
    __metaclass__ = SwitchboardMeta
    def awesome(self):
        print "I'm the child."
        super(Child, self).awesome()

if __name__ == '__main__':
    child = Child()
    child.awesome()
