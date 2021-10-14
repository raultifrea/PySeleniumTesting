import unittest

from FlightRadar24.Pages.Airlines import Defs


class Test_Names_of_Airlines(unittest.TestCase):

    def test_name_of_Airlines(self):
        test = Defs()
        test.load()
        test.get_names_of_airlines()
        test.quit()
