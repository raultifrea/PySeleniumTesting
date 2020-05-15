from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestATCBoundaries(unittest.TestCase):

    def testATCBoundaries(self):
        test = Defs()
        test.load()
        test.login()
        time.sleep(5)

        test.click_settings_button()
        test.click_atc_boundaries_button()

        list_of_atc_boundaries = test.get_list_of_atc_boundaries

        test.check_dropdown_functionality(list_of_atc_boundaries, "None")
        test.quit()