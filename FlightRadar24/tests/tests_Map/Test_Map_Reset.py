import unittest

from FlightRadar24.Pages.Map import Defs


class TestMapReset(unittest.TestCase):

    def testMapReset(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.check_reset_functionality()
        test.quit()
