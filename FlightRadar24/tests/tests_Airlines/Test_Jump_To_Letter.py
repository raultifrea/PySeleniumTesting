from FlightRadar24.Pages.Airlines import Defs
import unittest

class TestJumpToLetter(unittest.TestCase):

    letter = "t"

    def testJumpToLetter(self):
        test = Defs()
        test.load()
        test.click_selected_letter(self.letter)
        test.quit()