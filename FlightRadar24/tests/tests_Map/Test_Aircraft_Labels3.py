from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAircraftLabels3(unittest.TestCase):

    def testAircraftLabels3(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aircraft_labels_button_3
        list_of_aircraft_labels = test.get_list_of_aircraft_labels_3

        test.check_dropdown_functionality(list_of_aircraft_labels(), click)
        test.quit()