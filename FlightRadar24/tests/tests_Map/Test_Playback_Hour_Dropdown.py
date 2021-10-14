import unittest

from FlightRadar24.Pages.Map import Defs


class TestPlaybackHourDropdown(unittest.TestCase):

    def testPlaybackHourDropdown(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.check_dropdown_functionality(the_list=test.get_list_of_playback_hours(),
                                          click=test.click_playback_hour_button)
        test.quit()
