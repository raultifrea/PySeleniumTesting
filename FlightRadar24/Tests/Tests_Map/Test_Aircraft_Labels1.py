from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestAircraftLabels1(unittest.TestCase):

    def testAircraftLabels1(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()

        click = test.click_aircraft_labels_button_1
        list_of_aircraft_labels = test.get_list_of_aircraft_labels_1

        test.check_dropdown_functionality(list_of_aircraft_labels(), click)
        test.quit()