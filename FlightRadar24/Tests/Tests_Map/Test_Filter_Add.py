from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestFilterAdd(unittest.TestCase):

    filter_type = 'airport'
    '''
    filter type can be: callsign (e.g. SAS107), airport (e.g CLJ), altitude (km), speed (km/h)
    aircraft (e.g b737), registration (e.g HA-LYE) or radar
    '''
    input_text = 'clj'
    inout = 'in'

    def testFilterAdd(self):

        test = Defs()
        test.load()
        test.login()
        test.check_filter_functionality(self.filter_type, self.input_text, self.inout)
        time.sleep(3)

        test.quit()