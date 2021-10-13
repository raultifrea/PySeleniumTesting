from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestBookmarksMoveDown(unittest.TestCase):

    search = 'Schiphol'

    def testBookmarksMoveDown(self):

        test = Defs()

        test.load()
        test.login()
        test.click_bookmarks_button()

        test.click_bookmarks_manage_tab_button()
        test.manipulate_bookmark(self.search, func=test.click_movedown_bookmark)
        test.quit()