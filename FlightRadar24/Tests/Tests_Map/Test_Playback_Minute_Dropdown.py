from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestPlaybackMinuteDropdown(unittest.TestCase):

    def testPlaybackMinuteDropdown(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.check_dropdown_functionality(the_list=test.get_list_of_playback_minutes(), click=test.click_playback_minute_button)
        test.quit()