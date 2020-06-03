from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestBookmarksMoveUp(unittest.TestCase):

    search = 'Schiphol'

    def testBookmarksMoveUp(self):

        test = Defs()

        test.load()
        test.login()
        test.click_bookmarks_button()

        test.click_bookmarks_manage_tab_button()
        test.manipulate_bookmark(self.search, func=test.click_moveup_bookmark)
        test.quit()