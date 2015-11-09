
# Copyright (c) 2015 Joakim Gross, joakimgross@gmail.com
# File under MIT license, see the file LICENSE from this package for details.


class Simple(object):

    def add(self, x, y):
        return x + y


class SimpleWithDependency(object):
    """Class that needs an external dependency to be initialized
       before it can be used.
    """

    def __init__(self, dep):
        self.dep = dep

    def add(self, x, y):
        if self.dep.initialize() == True:
            return x + y
        else:
            return False

