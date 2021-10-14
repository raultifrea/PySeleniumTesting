import unittest

from FlightRadar24.Pages.Map import Defs


class TestURL(unittest.TestCase):

    def testURL(self):
        test = Defs()
        test.load()
        test.quit()

# if __name__ == '__main__':
#     unittest.main()
