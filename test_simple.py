
# Copyright (c) 2015 Joakim Gross, joakimgross@gmail.com
# File under MIT license, see the file LICENSE from this package for details.


from simple import Simple, SimpleWithDependency


class TestSimple(object):
    """Very simple unit test example."""

    def test_simple_add(self):
        s = Simple()
        assert s.add(1, 1) == 2


class TestSimpleWithDependency(object):
    """Simple unit test examples using stubs and mocks."""

    def test_simple_add_using_stub(self):
        """The class SimpleWithDependency gets its dependency
           as a stub we implement ourselves in the test suite.
           This is good when we need to have total controll of
           how the dependency acts and when the implementation
           will not involve too much code.
        """
        dep_stub = DependencyStub()
        s = SimpleWithDependency(dep_stub)
        assert s.add(1, 1) == 2

    def test_simple_add_using_mock(self, mocker):
        """The class SimeWithDependency gets its dependency
           as a mock object. This is good when we don't really
           care about the implementation of the dependency class
           but just need to replace the normal implementation.
        """
        dep_mock = mocker.MagicMock()
        s = SimpleWithDependency(dep_mock)
        s.add(1, 1)
        assert dep_mock.initialize.call_count == 1


class DependencyStub(object):
    """Stub implementation used in tests."""

    def initialize(self):
        return True

