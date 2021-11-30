import re


class ValidatePassword:
    def ValidPassword(self, p):
        """
        >>> v.ValidPassword("Q1@ertyuiop")
        True

        Password must be at least 8 characters
        >>> v.ValidPassword("Q1@erty")
        False

        Password must have at least 1 capital letter, 1 number and 1 special character
        >>> v.ValidPassword("Q@ertsdwerey")
        False
        >>> v.ValidPassword("1@ertyaaasdwe")
        False
        >>> v.ValidPassword("Qe1rtyuiopasd")
        False

        Password must be a string
        >>> v.ValidPassword(["Q@1rtyuiopasd"])
        Traceback (most recent call last):
            ...
        TypeError: Password must be a string
        >>> v.ValidPassword({"pass": "Q@1rtyuiopasd"})
        Traceback (most recent call last):
            ...
        TypeError: Password must be a string
        >>> v.ValidPassword(1234567890)
        Traceback (most recent call last):
            ...
        TypeError: Password must be a string
        >>> v.ValidPassword(0.123589712376)
        Traceback (most recent call last):
            ...
        TypeError: Password must be a string
        """

        if not isinstance(p, str):
            raise TypeError("Password must be a string")
        valid = False
        if len(p) > 7:
            chars = re.compile("[$&+,:;=?@#|'<>.^*()%!-]")
            upper = re.compile("[A-Z]")
            num = re.compile("[0-9]")
            if re.search(chars, p) and re.search(upper, p) and re.search(num, p):
                valid = True
        return valid


if __name__ == "__main__": #pragma: no cover
    import doctest
    # passd = ValidatePassword()
    # print(passd.ValidPassword(["Q@1jhgbsdjhasd"]))
    doctest.testmod(extraglobs={'v': ValidatePassword()})
