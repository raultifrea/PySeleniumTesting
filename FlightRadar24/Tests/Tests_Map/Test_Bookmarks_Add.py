from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestBookmarksAdd(unittest.TestCase):

    search = 'Schiphol'

    def testBookmarksAdd(self):

        test = Defs()

        test.load()
        test.login()
        test.perform_search(self.search)

        test.click_bookmarks_button()
        test.click_bookmarks_add_tab_button()
        test.send_keys_bookmarks_input_button(self.search)

        test.click_bookmarks_manage_tab_button()
        test.check_presence_of_new_bookmark(self.search)

        test.quit()