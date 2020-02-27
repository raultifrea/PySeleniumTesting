# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, HtmlTestRunner

from Digi24.Pages.Digi24_Meteo import Defs


class TestMeteoPressureBanat(unittest.TestCase):
    def test_meteo_pressure_Banat(self):
        meteo_transilvania = Defs()
        meteo_transilvania.load()
        meteo_transilvania.get_Regions("BANAT")
        meteo_transilvania.run_pressures()
        meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main()


