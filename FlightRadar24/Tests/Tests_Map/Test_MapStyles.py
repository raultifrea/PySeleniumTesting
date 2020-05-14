from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMapStyles(unittest.TestCase):

    def testMapStyles(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.check_map_style_functionality("Hybrid")
        time.sleep(3)
        test.quit()