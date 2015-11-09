(c) 2015 Joakim Gross, joakimgross@gmail.com <br>
Licensed under http://creativecommons.org/licenses/by-sa/4.0/ <br>
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)


TDD/Unit test Examples
======================

This repository contains code examples and instructions
used in a TDD guest lecture and is intended to be used
by attendees for reference and experimentation with the
concepts introduced.

This readme is formatted in a way intended to look nice
when rendered as markdown.

Setup
-----

Examples in this repo are tested on Ubuntu 15.04.

To start experimenting with the examples in this repo,
the required dependencies needs to be installed and
an environment set up. Below are steps for doing that
using `virtualenv` to create an isloated environment for
python (using `virtualenv` is not actually required but
can be nice if one feels uncertain about how the libraries
and tools will affect the environment):

```bash
    apt-get install python-pip
    pip install virtualenv
```

Set up a directory where a virtualenv will be created:

```bash
    virtualenv ~/tdd-env
    source ~/tdd-env/bin/activate
```

A virtualenv should now has been set up (to 'exit' from it,
type `deactivate` in the same terminal session as it was
created).

Install the required tools in the virtualenv:

```bash
    pip install pytest
    pip install pytest-mock
```

Run examples
------------

To run the unit tests, go to the root of this repo and type:

```bash
    py.test -v
```

List of examples
----------------

Directory contains the following modules:  

 * simple.py - Simple python module with two very basic classes.
 * test_simple.py - Contains unit tests for the simple module.
 * problematic.py - Python module with a slightly triky external dependency.
 * test_problematic.py - Contains unit tests for the problematic module.

Start with the simple.py module implementation and then check how
it's tested with test_simple.py. This test shows very simplistic
examples of a unit test, a test using a stub, and a test using a mock.

Check out problematic.py and its tests in test_problematic.py for
an example of monkeypatching to handle dependencies, again very
simplified.


