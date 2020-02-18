# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

class Defs:
    URL = 'https://www.digi24.ro'
    GDPR_locator = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Currency_type_locator = (By.XPATH, ".//*[@class='widget-exchange-rate-title']")
    Currency_value_locator = (By.XPATH, ".//*[@class='widget-exchange-rate-title']/descendant::strong")
    Currency_header_locator = (By.XPATH, ".//*[@class='widget widget-exchange']//following::span")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.GDPR_locator).click()

    def get_header_name(self):
        print(self.driver.find_element(*self.Currency_header_locator).text+'\n')

    def quit(self):
        self.driver.quit()