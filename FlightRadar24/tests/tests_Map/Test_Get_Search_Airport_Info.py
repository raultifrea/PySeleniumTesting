from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestGetSearchAirportInfo(unittest.TestCase):

    Airport = "malmo"

    def testGetSearchAirportInfo(self):

        test = Defs()
        test.load()
        test.login()
        test.perform_search(self.Airport)
        test.click_button_multiple_times(button=test.click_zoom_in_button, times=5)
        time.sleep(3)
        test.get_searched_airport_info(self.Airport)
        test.quit()