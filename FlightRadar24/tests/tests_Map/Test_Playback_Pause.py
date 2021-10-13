from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestPlaybackPausePlay(unittest.TestCase):

    def testPlaybackPausePlay(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.click_playback_start_button()
        test.click_playback_play_pause_button()
        time.sleep(3)
        test.quit()