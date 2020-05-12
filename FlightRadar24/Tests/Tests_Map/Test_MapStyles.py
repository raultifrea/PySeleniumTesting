from FlightRadar24.Pages.Map import Defs
import unittest

class TestMapStyles(unittest.TestCase):

    def testMapStyles(self):
        test = Defs()
        test.load()
        test.check_map_style_functionality("Satellite")
        test.quit()