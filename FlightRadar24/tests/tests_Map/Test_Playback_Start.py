from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestPlaybackStart(unittest.TestCase):

    def testPlaybackStart(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.click_playback_start_button()
        test.wait_for_playback_controls_overlay()
        test.quit()