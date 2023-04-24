from coolpkg.core.code import awesome_function
from unittest import TestCase

class TestAwesomeFunction(TestCase):
    def test_func(self) -> None:
        self.assertEqual(4, awesome_function(3, 1))
