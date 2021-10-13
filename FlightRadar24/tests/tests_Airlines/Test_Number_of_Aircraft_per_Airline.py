from FlightRadar24.Pages.Airlines import Defs
import unittest

class TestNumberOfAircraftPerAirline(unittest.TestCase):

    airline = "Tarom"

    def testNumberOfAircraftPerAirline(self):
        test = Defs()
        test.load()
        test.get_number_of_aircrafts_per_airline(self.airline)
        test.quit()