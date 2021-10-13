from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestWeatherChangeToggleState(unittest.TestCase):

    Title = ["Cloud", "Total precipitation", "Intense precipitation", "North American radar", "Australian radar",
             "Lightning", "AIRMETs/SIGMETs", "High level significant weather"]

    def testWeatherChangeToggleState(self):
        test = Defs()

        test.load()
        test.login()
        test.click_settings_button()
        test.click_weather_button()

        lista = test.get_list_of_weather_toggles

        test.change_toggle_button_state(lista, self.Title)
        test.quit()