from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestBookmarksRemove(unittest.TestCase):

    search = 'Romania'

    def testBookmarksRemove(self):

        test = Defs()

        test.load()
        test.login()
        test.click_bookmarks_button()
        test.click_bookmarks_manage_tab_button()
        test.delete_bookmark(self.search)


        test.quit()