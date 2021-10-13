from FlightRadar24.Pages.Map import Defs
import unittest

class TestFullScreenPopup(unittest.TestCase):

    title = 'Full-screen view'

    def testFullScreenPopup(self):

        test = Defs()
        test.load()
        test.check_full_screen_title_text(self.title)
        test.quit()