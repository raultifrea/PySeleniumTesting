import unittest

from FlightRadar24.Pages.Map import Defs


class TestVisibilityChangeToggleState(unittest.TestCase):

    def testVisibilityChangeToggleState(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()
        test.click_visibility_button()

        lista = test.get_list_of_visibility_toggles

        test.change_toggle_button_state(lista)
        test.quit()
