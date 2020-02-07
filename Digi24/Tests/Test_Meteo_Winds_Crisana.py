# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

from Digi24.Pages.Meteo_Romania import Defs

class TestMeteoPressureCrisana(unittest.TestCase):

    meteo_transilvania = Defs()
    meteo_transilvania.load()
    meteo_transilvania.get_Regions("CRIȘANA")
    meteo_transilvania.run_winds()
    meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main()


