# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from Digi24.Pages.Meteo import Defs


class Test_Meteo_Transilvania(unittest.TestCase):

    pressures_list = []
    temperatures_list = []
    winds_list = []
    #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Transilvania')
    os.chdir(r'C:\Users\F73482\Desktop\Meteo')

    meteo_romania = Defs()
    meteo_romania.load()
    meteo_romania.center_element()
    meteo_romania.run_pressure()
    meteo_romania.quit()

if __name__ == "__main__":
    unittest.main()


