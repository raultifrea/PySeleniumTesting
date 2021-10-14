import unittest

from FlightRadar24.Pages.Map import Defs


class TestMiscDropdowns(unittest.TestCase):

    def testMiscDropdowns(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        test.click_misc_button()
        test.check_misc_dropdown_functionality()
        test.quit()
