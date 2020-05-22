from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMapBrightness(unittest.TestCase):

    def testMapBrightness(self):
        test = Defs()
        test.load()
        test.click_settings_button()

        slider = test.brightness_button_slider

        time.sleep(3)
        test.drag_and_drop_slider(500, slider)
        time.sleep(3)
        test.quit()