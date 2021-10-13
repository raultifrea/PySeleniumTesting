from FlightRadar24.Pages.Map import Defs
import unittest


class TestSettingsChangeToggleState(unittest.TestCase):

    Title = ["Oceanic tracks"]

    def testSettingsChangeToggleState(self):
        test = Defs()
        test.load()
        test.click_settings_button()

        lista = test.get_list_of_toggles

        test.change_toggle_button_state(lista, self.Title)
        test.quit()