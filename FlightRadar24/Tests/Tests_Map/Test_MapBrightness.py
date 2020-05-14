from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMapBrightness(unittest.TestCase):

    def testMapBrightness(self):
        test = Defs()
        test.load()
        test.click_settings_button()

        slider = test.brightness_button_slider
        test.drag_and_drop_slider(500, slider)
        time.sleep(5)
        test.quit()