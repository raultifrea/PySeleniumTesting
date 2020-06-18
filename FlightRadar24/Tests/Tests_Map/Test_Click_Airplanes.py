from FlightRadar24.Pages.Map import Defs
import unittest, time


class TestClickAirplanes(unittest.TestCase):

    def testClickAirplanes(self):

        test = Defs()

        test.load()
        test.login()


        test.perform_search("cluj")
        test.click_airport_close_button()



        test.click_airplanes()

        test.close_full_screen()
        test.quit()