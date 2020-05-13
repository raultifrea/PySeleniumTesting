from FlightRadar24.Pages.Map import Defs
import unittest

class TestMapBrightness(unittest.TestCase):

    def testMapBrightness(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.click_brightness_button()
        test.quit()