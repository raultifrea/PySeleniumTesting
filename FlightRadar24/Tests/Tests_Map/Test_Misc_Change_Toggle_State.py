from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestMiscChangeToggleState(unittest.TestCase):


    def testMiscChangeToggleState(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()
        test.click_misc_button()

        lista = test.get_list_of_misc_toggles

        test.change_toggle_button_state(lista)
        test.quit()