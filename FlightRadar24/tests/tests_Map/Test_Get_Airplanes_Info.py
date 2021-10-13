from FlightRadar24.Pages.Map import Defs
import unittest


class TestGetAirplanesInfo(unittest.TestCase):

    City = 'cluj'

    def testGetAirplanesInfo(self):

        test = Defs()

        test.load()
        test.login()
        test.perform_search(self.City)

        test.click_airport_close_button()
        test.get_airplanes_info()
        test.close_full_screen()

        test.quit()