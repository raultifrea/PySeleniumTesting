from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestPlaybackClose(unittest.TestCase):

    def testPlaybackClose(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.click_playback_start_button()
        test.click_playback_close_button()
        time.sleep(3)
        test.quit()