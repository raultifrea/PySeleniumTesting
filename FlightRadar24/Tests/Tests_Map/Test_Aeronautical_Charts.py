from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAeronauticalCharts(unittest.TestCase):

    def testAeronauticalCharts(self):
        test = Defs()

        test.load()
        test.login()
        test.wait_for_login_refresh()

        test.click_settings_button()
        test.click_aeronautical_charts_button()

        list_of_aeronautical_charts = test.get_list_of_aeronautical_charts

        test.check_dropdown_functionality_old(list_of_aeronautical_charts, "None")
        test.quit()