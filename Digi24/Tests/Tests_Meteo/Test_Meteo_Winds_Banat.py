# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

from Digi24.Pages.Digi24_Meteo import Defs


class TestMeteoWindsBanat(unittest.TestCase):

    meteo_transilvania = Defs()
    meteo_transilvania.load()
    meteo_transilvania.get_Regions("BANAT")
    meteo_transilvania.run_winds()
    meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main()


