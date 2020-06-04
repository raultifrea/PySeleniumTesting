from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestPlaybackSpeedDropdown(unittest.TestCase):

    def testPlaybackSpeedDropdown(self):
        test = Defs()

        test.load()
        test.login()
        test.click_playback_button()
        test.check_dropdown_functionality(the_list=test.get_list_of_playback_speeds(), click=test.click_playback_speed_button)
        test.quit()