from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestSearch(unittest.TestCase):

    def testSearch(self):

        test = Defs()
        test.load()
        test.login()
        test.perform_search("heathrow")
        test.quit()