from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestClickAirportPins(unittest.TestCase):

    def testClickAirportPins(self):

        test = Defs()

        test.load()
        test.login()
        test.click_airport_pins()
        test.quit()