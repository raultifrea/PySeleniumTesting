from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAircraftSizes(unittest.TestCase):

    def testAircraftSizes(self):
        test = Defs()

        test.load()
        test.login()
        test.wait_for_login_refresh()
        test.click_settings_button()

        click = test.click_aircraft_sizes_button
        list_of_aircraft_sizes = test.get_list_of_aircraft_sizes

        click()
        test.check_dropdown_functionality(list_of_aircraft_sizes(), click)
        test.quit()