from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMapStyles(unittest.TestCase):

    def testMapStyles(self):
        test = Defs()

        test.load()
        test.login()
        time.sleep(5)

        test.click_settings_button()
        test.click_map_style_button()

        list_of_map_styles = test.get_list_of_map_styles

        test.check_dropdown_functionality(list_of_map_styles, "Hybrid")
        test.quit()