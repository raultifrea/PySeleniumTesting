import unittest

from FlightRadar24.Pages.Map import Defs


class TestPlaybackZoom(unittest.TestCase):

    def testPlaybackZoom(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.click_playback_start_button()
        test.click_button_multiple_times(button=test.click_playback_zoomin_button, times=3)
        test.click_button_multiple_times(button=test.click_playback_zoomout_button, times=3)
        test.quit()
