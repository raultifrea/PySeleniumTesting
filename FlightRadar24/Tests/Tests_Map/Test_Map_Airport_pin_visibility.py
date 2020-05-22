from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMapAirportPinVisibility(unittest.TestCase):

    def testMapAirportPinVisibility(self):
        test = Defs()
        test.load()
        test.click_settings_button()

        slider = test.airport_pin_visilibity_slider

        time.sleep(3)
        test.drag_and_drop_slider(500, slider)
        time.sleep(3)
        test.quit()