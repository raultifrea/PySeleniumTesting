import time
import unittest

from FlightRadar24.Pages.Map import Defs


class TestPlaybackPausePlay(unittest.TestCase):

    def testPlaybackPausePlay(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()

        test.click_playback_start_button()
        test.drag_and_drop_slider(100, slider=test.playback_slider, slidebar=test.playback_slidebar)
        time.sleep(3)

        test.quit()
