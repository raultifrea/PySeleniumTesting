import unittest

from FlightRadar24.Pages.Map import Defs


class TestATCBoundaries(unittest.TestCase):
    Title = ["ATC boundaries"]

    def testATCBoundaries(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_atc_boundaries_button
        list_of_atc_boundaries = test.get_list_of_atc_boundaries

        test.check_dropdown_functionality(list_of_atc_boundaries(), click, self.Title)
        test.quit()
