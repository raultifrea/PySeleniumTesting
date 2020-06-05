from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestZoomOut(unittest.TestCase):

    def testZoomOut(self):
        test = Defs()

        test.load()
        test.click_button_multiple_times(button=test.click_zoom_out_button, times=5)
        test.wait_for_text_to_change(element=test.current_nb_of_aircraft_on_map)
        test.quit()