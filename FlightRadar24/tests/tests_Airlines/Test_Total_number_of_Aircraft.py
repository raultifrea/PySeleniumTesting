import unittest

from FlightRadar24.Pages.Airlines import Defs


class TestTotalNumberOfAircraft(unittest.TestCase):

    def testTotalNbAircraft(self):
        test = Defs()
        test.load()
        test.get_total_nb_aircrafts()
        test.quit()
