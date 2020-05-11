from FlightRadar24.Pages.Airlines import Defs
import unittest

class TestNumberOfAirlines(unittest.TestCase):

    def testNbAirlines(self):
        test = Defs()
        test.load()
        test.return_nb_of_airlines()
        test.quit()