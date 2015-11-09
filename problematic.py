
# Copyright (c) 2015 Joakim Gross, joakimgross@gmail.com
# File under MIT license, see the file LICENSE from this package for details.


class Problematic(object):
    """Problematic class that will block tests when calling
       into external class.
    """

    def add_using_external_dependency(self, x, y):
        some_library_loop = InfiniteLoopLibrary()
        some_library_loop.run()
        return x + y


class InfiniteLoopLibrary(object):
    """Represents a class that enters an infinite
       loop meant to represent e.g. a mainloop.

       Typically this class would reside in some external
       library or binding.
    """

    def run(self):
        while True:
            pass

