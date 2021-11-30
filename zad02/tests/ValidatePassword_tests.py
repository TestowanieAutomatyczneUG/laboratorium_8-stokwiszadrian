import unittest
from src import ValidatePassword


class ValidatePasswordTest(unittest.TestCase):
    def setUp(self):
        self.valid = ValidatePassword.ValidatePassword()

    def test_validate_validpass(self):
        self.assertTrue(self.valid.ValidPassword("Q1@ertyuiop"))

    def test_validate_len_lessthan8(self):
        self.assertFalse(self.valid.ValidPassword("Q1@ert"))

    def test_validate_no_capital(self):
        self.assertFalse(self.valid.ValidPassword("1@ertyuiop"))

    def test_validate_no_number(self):
        self.assertFalse(self.valid.ValidPassword("Q@ertyuiop"))

    def test_validate_no_special_char(self):
        self.assertFalse(self.valid.ValidPassword("Q1ertyuiop"))

    def test_validate_wrongtype_int(self):
        self.assertRaises(TypeError, self.valid.ValidPassword, 12355635)

    def test_validate_wrongtype_array(self):
        self.assertRaises(TypeError, self.valid.ValidPassword, ["QW@#r234tdfsd"])

    def test_validate_wrongtype_dict(self):
        self.assertRaises(TypeError, self.valid.ValidPassword, {"pass": "Q@#we44sadaa"})

    def test_validate_wrongtype_float(self):
        self.assertRaises(TypeError, self.valid.ValidPassword, 234.9872364)

    def test_validate_wrongtype_tuple(self):
        self.assertRaises(TypeError, self.valid.ValidPassword, ("kjashdj", "9Wq!234"))

    def tearDown(self):
        self.valid = None
