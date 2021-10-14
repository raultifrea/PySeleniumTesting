import time
import unittest

from FlightRadar24.Pages.Map import Defs


class TestMapBrightness(unittest.TestCase):

    def testMapBrightness(self):
        test = Defs()

        test.load()
        test.click_settings_button()
        time.sleep(3)

        test.drag_and_drop_slider(500, slider=test.brightness_button_slider, slidebar=test.map_slidebar)
        time.sleep(3)
        test.quit()
