import time
import unittest

from FlightRadar24.Pages.Map import Defs


class TestFilterAddGuest(unittest.TestCase):
    filter_type = 'altitude'
    '''
    filter type can be: callsign (e.g. SAS107), airport (e.g CLJ), altitude (km), speed (km/h)
    aircraft (e.g b737), registration (e.g HA-LYE) or radar
    '''
    input_text = ''
    inout = ''
    text = 'If you want to set more filters, please check out our subscription plans.'

    def testFilterAddGuest(self):
        test = Defs()
        test.load()
        test.check_filter_functionality(self.filter_type, self.input_text, self.inout)
        test.check_filter_limit_text(self.text)
        time.sleep(3)

        test.quit()
