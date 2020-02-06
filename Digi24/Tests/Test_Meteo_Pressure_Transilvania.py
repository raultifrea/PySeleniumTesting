# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from personalprojects.Digi24.Pages.Meteo_Romania import Defs


class TestMeteoPressureTransilvania(unittest.TestCase):

    os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Transilvania')
    #os.chdir(r'C:\Users\F73482\Desktop\Meteo\Transilvania')

    meteo_transilvania = Defs()
    meteo_transilvania.load()
    #meteo_transilvania.center_element()
    meteo_transilvania.get_Regions("TRANSILVANIA")
    meteo_transilvania.run_pressures()
    meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main()


