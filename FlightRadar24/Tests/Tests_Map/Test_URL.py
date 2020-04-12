from FlightRadar24.Pages.Map import Defs
import unittest

class TestURL(unittest.TestCase):

    def testURL(self):
        test = Defs()
        test.load()
        test.quit()