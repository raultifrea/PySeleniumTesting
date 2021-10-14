import unittest

from FlightRadar24.Pages.Map import Defs


class TestFullScreenPopup(unittest.TestCase):
    title = 'Full-screen view'

    def testFullScreenPopup(self):
        # deprecated

        test = Defs()
        test.load()
        test.check_full_screen_title_text(self.title)
        test.quit()
