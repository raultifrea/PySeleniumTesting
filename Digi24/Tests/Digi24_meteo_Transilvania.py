# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from personalprojects.Digi24.Pages.Digi24_meteo import Defs


class Test_Meteo_Transilvania(unittest.TestCase):

    pressures_list = []
    temperatures_list = []
    winds_list = []
    #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Transilvania')
    current_day = str(datetime.datetime.now())[:11]  # takes only the yyyy-mm-dd values of the date

    meteo_romania = Defs()
    meteo_romania.load()
    meteo_romania.center_element()
    meteo_romania.quit()

if __name__ == "__main__":
    unittest.main()


