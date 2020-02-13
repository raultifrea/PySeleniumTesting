# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from Digi24.Pages.Meteo_Romania import Defs

class TestMeteoTemperatureRomania(unittest.TestCase):

    meteo_romania = Defs()
    meteo_romania.load()
    meteo_romania.center_element()
    meteo_romania.run_temperatures()
    meteo_romania.quit()

if __name__ == "__main__":
    unittest.main()


