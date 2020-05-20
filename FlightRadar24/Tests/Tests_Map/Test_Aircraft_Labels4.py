from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAircraftLabels4(unittest.TestCase):

    def testAircraftLabels4(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aircraft_labels_button_4
        list_of_aircraft_labels = test.get_list_of_aircraft_labels_4

        test.check_dropdown_functionality(list_of_aircraft_labels(), click)
        test.quit()