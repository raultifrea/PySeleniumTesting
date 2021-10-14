import unittest

from FlightRadar24.Pages.Map import Defs


class TestAircraftSizes(unittest.TestCase):

    def testAircraftSizes(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aircraft_sizes_button
        list_of_aircraft_sizes = test.get_list_of_aircraft_sizes

        test.check_dropdown_functionality(list_of_aircraft_sizes(), click)
        test.quit()
