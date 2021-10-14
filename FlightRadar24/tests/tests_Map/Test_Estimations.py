import unittest

from FlightRadar24.Pages.Map import Defs


class TestEstimations(unittest.TestCase):

    def testEstimations(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()
        test.click_visibility_button()

        click = test.click_estimations_button
        list_of_aircraft_labels = test.get_list_of_estimations

        test.check_dropdown_functionality(list_of_aircraft_labels(), click)
        test.quit()
