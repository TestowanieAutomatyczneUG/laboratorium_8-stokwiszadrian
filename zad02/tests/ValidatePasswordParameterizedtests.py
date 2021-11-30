import unittest, sys
from parameterized import parameterized, parameterized_class
from assertpy import assert_that

import math

sys.path.append("../src")
from ValidatePassword import ValidatePassword

# Ten test zostanie wykonany, gdy użyjemy nosetests
@parameterized([
    ("32ssA22$@#aa", True),
    ("34a@@Q", False),
    ("aass@@Qgdsx", False),
    ("asbsd@1laksjf", False)
])
def test_ValidatePassword_func(password, expected):
    temp = ValidatePassword()
    assert_that(temp.ValidPassword(password)).is_equal_to(expected)


class ValidatePasswordParameterized(unittest.TestCase):

    def setUp(self):
        self.tmp = ValidatePassword()

    @parameterized.expand([
        ("aOO22$@#aa", True),
        ("34@@Q", False),
        ("aass@@Qgdsx", False),
    ])
    def test_ValidatePassword_Parameterized(self, password, expected):
        self.assertEqual(self.tmp.ValidPassword(password), expected)


@parameterized_class(('password', 'expected'), [
    ("aQ!2kajsbf", True),
    ("aq@3ss", False),
    ("dg34623@@", False),
    ("aQQ123oooo", False),
    ("aQQ!!kajsbhf", False)
])
class ValidatePasswordParameterizedClass(unittest.TestCase):
    def setUp(self):
        self.tmp = ValidatePassword()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.ValidPassword(self.password), self.expected)


if __name__ == '__main__':
    unittest.main()
