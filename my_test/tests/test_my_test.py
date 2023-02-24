"""
Unit and regression test for the my_test package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import my_test


def test_my_test_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", my_test.__name__)
    assert "my_test" in sys.modules


# Assert that a certain exception is raised
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
