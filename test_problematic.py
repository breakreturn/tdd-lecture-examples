
# Copyright (c) 2015 Joakim Gross, joakimgross@gmail.com
# File under MIT license, see the file LICENSE from this package for details.


import pytest

from problematic import Problematic


class TestProblematic(object):
    """Shows various ways to test the Problematic class

       When testing the Problematic class, it would normally
       block execution when calling into an external dependency
       which contains an infinite loop. The test methods in this
       class shows different ways of how to test it.
    """

    @pytest.mark.skipif("True")
    def test_problematic_add(self):
        """"This test would block the test suite and serves as an
            example of the problem. The test is skipped.
        """
        p = Problematic()
        assert p.add_using_external_dependency(1, 1) == 2

    def test_problematic_add_using_patch(self, mocker):
        """This test patches, i.e. replaces, the problematic code so
           the tests can be carried out.
        """
        # 'mocker' fixture can be used by taking it as an argument, see
        # https://github.com/pytest-dev/pytest-mock/
        mocker.patch("problematic.InfiniteLoopLibrary")
        # problematic.InfiniteLoopLibrary class is now replaced
        # with a mock.MagicMock object when it is instantiated by
        # problematic.Problematic, see
        # http://www.voidspace.org.uk/python/mock/patch.html#patch
        p = Problematic()
        assert p.add_using_external_dependency(1, 1) == 2
        # The MagicMock instance allowed the otherwise blocking
        # calls in Problematic.add_using_external_dependency
        # to be made without anything really happening and thus
        # allowing the code execution to continue to the actual
        # code we want to test.

