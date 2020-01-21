# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from personalprojects.Digi24.Tests.Digi24_meteo import Test_Meteo_Romania


class Test_Meteo_Transilvania(unittest.TestCase,Test_Meteo_Romania):

    pressures_list = []
    temperatures_list = []
    winds_list = []
    os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Transilvania')
    current_day = str(datetime.datetime.now())[:11]  # takes only the yyyy-mm-dd values of the date
    open(current_day + ".txt", "w").close()  # deletes content before running the script again
    with open(current_day + ".txt", 'a+', encoding="utf-8") as file:
        print("Timestamp: " + str(datetime.datetime.now())[:19] + "\n", file=file)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.digi24.ro/meteo/transilvania")
        self.driver.find_element_by_xpath(".//*[@class='gdpr-button gdpr-trigger']").click()  # GDPR prompt dismissal
        center_element = self.driver.find_element_by_xpath(".//*[@class='weather-map-pin weather-map-pin-sibiu']")  # finds a central element on the page
        actions = ActionChains(self.driver)
        actions.move_to_element(center_element).perform()  # scrolls the page to the central element


    Test_Meteo_Romania().test_atm_pressures()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


