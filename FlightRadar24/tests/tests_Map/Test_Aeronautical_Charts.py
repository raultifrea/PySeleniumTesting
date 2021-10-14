import unittest

from FlightRadar24.Pages.Map import Defs


class TestAeronauticalCharts(unittest.TestCase):
    Title = ["Navaids", "Low altitude charts", "High altitude charts"]

    def testAeronauticalCharts(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aeronautical_charts_button
        list_of_aeronautical_charts = test.get_list_of_aeronautical_charts

        test.check_dropdown_functionality(list_of_aeronautical_charts(), click, self.Title)
        test.quit()
