import unittest

from FlightRadar24.Pages.Map import Defs


class TestPlaybackTimeline(unittest.TestCase):

    def testPlaybackTimeline(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.click_playback_start_button()
        test.click_button_multiple_times(button=test.click_playback_scroll_left_button, times=15)
        test.click_button_multiple_times(button=test.click_playback_scroll_right_button, times=15)
        test.quit()
