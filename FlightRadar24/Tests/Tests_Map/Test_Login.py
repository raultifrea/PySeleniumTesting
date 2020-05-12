from FlightRadar24.Pages.Map import Defs
import unittest

class TestLogin(unittest.TestCase):

    def testURL(self):
        test = Defs()
        test.load()
        test.login()
        test.quit()