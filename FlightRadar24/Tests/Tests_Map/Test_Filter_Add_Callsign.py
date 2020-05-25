from FlightRadar24.Pages.Map import Defs
import unittest

class TestFilterAddCallsign(unittest.TestCase):

    callsign = "csa3da"  # dynamic

    def testFilterAddCallsign(self):

        test = Defs()
        test.load()
        test.click_filter_button()
        test.click_filter_toggle()
        test.send_keys_filter_callsign_input(self.callsign.upper())
        test.click_filter_add_button()
        test.check_filter_text(self.callsign.upper())
        test.quit()