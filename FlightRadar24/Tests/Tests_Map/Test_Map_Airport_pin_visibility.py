from FlightRadar24.Pages.Map import Defs
import unittest, time

class TestMapAirportPinVisibility(unittest.TestCase):

    def testMapAirportPinVisibility(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.drag_and_drop_slider(500)
        time.sleep(3)
        test.quit()