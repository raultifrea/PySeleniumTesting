import unittest

from FlightRadar24.Pages.Map import Defs


class TestPlaybackDateDropdown(unittest.TestCase):
    title = 'Global playback'

    def testPlaybackDateDropdown(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.check_dropdown_functionality(the_list=test.get_list_of_playback_dates(),
                                          click=test.click_playback_date_button, title=self.title)
        test.quit()
