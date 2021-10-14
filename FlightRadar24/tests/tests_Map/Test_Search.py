import unittest

from FlightRadar24.Pages.Map import Defs


class TestSearch(unittest.TestCase):

    def testSearch(self):
        test = Defs()
        test.load()
        test.login()
        test.perform_search("heathrow")
        test.quit()
