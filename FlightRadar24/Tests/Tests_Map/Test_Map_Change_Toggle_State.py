from FlightRadar24.Pages.Map import Defs
import unittest

class TestMapChangeToggleState(unittest.TestCase):

    map_toggles = {'Day_night_line': 'fr24_showNightLine',
                   'Oceanic_tracks': 'fr24_showNDB',
                   'Airport_pins': 'fr24_showAirports',
                   'Animate_aircraft': 'fr24_animateAircraft',
                   'Aircraft_labels': 'fr24_showAircraftLabels',
                   'Label_background': 'fr24_showLabelBkg'}

    def testMapChangeToggleState(self):
        test = Defs()
        test.load()
        test.click_settings_button()
        test.change_toggle_button_state(self.map_toggles.get('Oceanic_tracks'))
        test.quit()