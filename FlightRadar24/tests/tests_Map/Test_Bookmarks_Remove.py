import unittest

from FlightRadar24.Pages.Map import Defs


class TestBookmarksRemove(unittest.TestCase):
    search = 'Schiphol'

    def testBookmarksRemove(self):
        test = Defs()

        test.load()
        test.login()
        test.click_bookmarks_button()

        test.click_bookmarks_manage_tab_button()
        test.manipulate_bookmark(self.search, func=test.click_delete_bookmark)
        test.quit()
