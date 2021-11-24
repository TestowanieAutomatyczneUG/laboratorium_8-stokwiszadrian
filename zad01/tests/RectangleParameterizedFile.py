import unittest
from sample.Rectangle import *

class RectangleParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/rectangle_data_test")
      tmpRectangle = Rect()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(",")
            inp1, inp2, result = int(data[0]) | bool(data[0]), int(data[1]) | bool(data[1]), data[2].rstrip('\n').encode("idna")
            if result == b"Exception":
                self.assertRaises(Exception, tmpRectangle.draw_rect, -4, 1)
            else:
                self.assertEqual(tmpRectangle.draw_rect(inp1, inp2).encode("unicode_escape"), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
