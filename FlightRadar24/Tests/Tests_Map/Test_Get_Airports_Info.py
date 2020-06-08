from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestGetAirportsInfo(unittest.TestCase):

    def testGetAirportsInfo(self):

        test = Defs()

        test.load()
        test.login()
        test.click_zoom_out_button()
        test.wait_for_text_to_change(element=test.current_nb_of_aircraft_on_map)
        test.get_airports_info()
        test.quit()