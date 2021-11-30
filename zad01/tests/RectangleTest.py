import unittest
from assertpy import assert_that
from sample.Rectangle import *

class RectTest(unittest.TestCase):
    def setUp(self):
        self.temp = Rect()

    def test_Rect_instance(self):
        assert_that(self.temp).is_instance_of(Rect)

    def test_Rect_positive_ab_equal(self):
        assert_that(self.temp.draw_rect(3, 3)).is_equal_to("***\n* *\n***\n")

    def test_Rect_positive_ab_different(self):
        assert_that(self.temp.draw_rect(3, 4)).is_equal_to("****\n*  *\n****\n")

    def test_Rect_positive_contains(self):
        assert_that(self.temp.draw_rect(4, 4)).starts_with("****").ends_with("****\n").contains("  ")

    def test_Rect_does_not_contain(self):
        assert_that(self.temp.draw_rect(4, 3)).does_not_contain("  ")

    def test_Rect_not_empty(self):
        assert_that(self.temp.draw_rect(1, 1)).is_not_empty()

    def test_Rect_not_None(self):
        assert_that(self.temp.draw_rect(2, 2)).is_not_none()

    def test_Rect_return_instance(self):
        assert_that(self.temp.draw_rect(3, 3)).is_instance_of(str).is_type_of(str)

    def test_Rect_wrongdirection(self):
        assert_that(self.temp.draw_rect(4, 3)).is_not_equal_to("****\n*  *\n****\n")

    def test_Rect_a_lessthanzero(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(-1, 4)

    def test_Rect_b_lessthanzero(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(4, -1)

    def test_Rect_a_float(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(0.5, 4)

    def test_Rect_b_float(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(4, 0.5)

    def test_Rect_args_list(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with([3, 2])

    def test_Rect_args_dict(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with({"a": 4, "b": 4})

    def test_Rect_args_None(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(None, 4)

    def test_Rect_args_True(self):
        assert_that(self.temp.draw_rect(True, 4)).is_not_empty()

    def test_Rect_args_allTrue(self):
        assert_that(self.temp.draw_rect(True, True)).is_equal_to("*\n")

    def test_Rect_args_False(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(False, 4)

    def test_Rect_args_None(self):
        assert_that(self.temp.draw_rect).raises(Exception).when_called_with(None)

    def tearDown(self):
        self.temp = None