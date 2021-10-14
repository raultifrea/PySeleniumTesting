import unittest

from FlightRadar24.Pages.Map import Defs


class TestFullScreen(unittest.TestCase):

    def testFullScreen(self):
        test = Defs()
        test.load()
        test.login()

        test.check_full_screen_functionality()
        test.quit()
