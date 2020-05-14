from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestATCBoundaries(unittest.TestCase):

    def testATCBoundaries(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.check_atc_boundaries_functionality("None")
        time.sleep(3)
        test.quit()