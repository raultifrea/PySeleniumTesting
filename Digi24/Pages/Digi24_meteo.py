# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from selenium.webdriver.common.by import By

class Defs:
    URL = 'https://www.digi24.ro/meteo'
    GDPR = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Center_Element = (By.XPATH, ".//*[@class='weather-map-pin weather-map-pin-sibiu")
    Pressure = (By.CLASS_NAME, "atmo")
    City = (By.CLASS_NAME, "city")
    Wind = (By.CLASS_NAME, "wind")
    Temperature = (By.CLASS_NAME,"temp")
    #To add loop through cities

    def __init__(self):
        self.driver = webdriver.Chrome()

    def center_element(self):
        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(self.Center_Element))
        self.driver.execute_script("window.scrollTo(0, 200)")

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.GDPR).click()

    def quit(self):
        self.driver.quit()






