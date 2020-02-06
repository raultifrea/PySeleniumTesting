# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from personalprojects.Digi24.Pages.Meteo_Romania import Defs


class TestMeteoPressureRomania(unittest.TestCase):

    os.chdir(r'C:\Users\tzifrea\Desktop\Meteo')
    #os.chdir(r'C:\Users\F73482\Desktop\Meteo')

    meteo_romania = Defs()
    meteo_romania.load()
    meteo_romania.center_element()
    meteo_romania.run_pressures()
    meteo_romania.quit()

if __name__ == "__main__":
    unittest.main()


