import unittest

from FlightRadar24.Pages.Map import Defs


class TestClickAirportPins(unittest.TestCase):

    def testClickAirportPins(self):
        test = Defs()

        test.load()
        test.login()
        test.click_airport_pins()
        test.quit()
