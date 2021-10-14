import unittest

from FlightRadar24.Pages.Airlines import Defs


class TestAverageNumberOfAircraft(unittest.TestCase):

    def testAvgNbAircraft(self):
        test = Defs()
        test.load()
        test.get_average_nb_aircrafts()
        test.quit()
