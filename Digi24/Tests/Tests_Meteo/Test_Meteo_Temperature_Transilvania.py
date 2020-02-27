# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

from Digi24.Pages.Digi24_Meteo import Defs


class TestMeteoTemperatureTransilvania(unittest.TestCase):
    def test_meteo_temperature_Transilvania(self):
        meteo_transilvania = Defs()
        meteo_transilvania.load()
        meteo_transilvania.get_Regions("TRANSILVANIA")
        meteo_transilvania.run_temperatures()
        meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main()


