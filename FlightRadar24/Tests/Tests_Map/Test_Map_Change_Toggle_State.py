from FlightRadar24.Pages.Map import Defs
import unittest


class TestMapChangeToggleState(unittest.TestCase):

    Title = ["Oceanic tracks"]

    def testMapChangeToggleState(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.change_toggle_button_state(self.Title)
        test.quit()