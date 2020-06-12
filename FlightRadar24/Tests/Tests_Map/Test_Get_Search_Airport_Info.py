from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestGetSearchAirportInfo(unittest.TestCase):

    Airport = "atlanta"

    def testGetSearchAirportInfo(self):

        test = Defs()
        test.load()
        test.login()
        test.perform_search(self.Airport)
        test.click_button_multiple_times(button=test.click_zoom_in_button, times=5)
        #test.wait_for_text_to_change(element=test.current_nb_of_aircraft_on_map)
        time.sleep(3)
        test.get_searched_airport_info(self.Airport)
        test.quit()