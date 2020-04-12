from FlightRadar24.Pages.Airlines import Defs
import unittest

class TestAvgNbAircraft(unittest.TestCase):

    def testAvgNbAircraft(self):
        test = Defs()
        test.load()
        test.get_average_nb_aircrafts()
        test.quit()