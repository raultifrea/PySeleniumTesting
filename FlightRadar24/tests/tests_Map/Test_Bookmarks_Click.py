import unittest

from FlightRadar24.Pages.Map import Defs


class TestBookmarksClick(unittest.TestCase):

    def testBookmarksClick(self):
        test = Defs()
        test.load()
        test.login()
        test.click_bookmarks()
        test.quit()
