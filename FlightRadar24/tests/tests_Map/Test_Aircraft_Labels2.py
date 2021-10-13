from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAircraftLabels2(unittest.TestCase):

    def testAircraftLabels2(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aircraft_labels_button_2
        list_of_aircraft_labels = test.get_list_of_aircraft_labels_2

        test.check_dropdown_functionality(list_of_aircraft_labels(), click)
        test.quit()