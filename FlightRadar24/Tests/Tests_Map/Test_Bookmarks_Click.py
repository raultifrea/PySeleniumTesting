from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestBookmarksClick(unittest.TestCase):

    def testBookmarksClick(self):

        test = Defs()
        test.load()
        test.click_bookmarks()
        test.quit()