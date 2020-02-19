# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import os, datetime

class Defs:
    URL = 'https://www.digi24.ro'
    GDPR_locator = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Currency_type_locator = (By.XPATH, ".//*[@class='widget-exchange-rate-title']")
    Currency_header_locator = (By.XPATH, ".//*[@class='widget widget-exchange']//following::span")
    Weather_header_locator = (By.XPATH, ".//*[@class='widget widget-weather']//descendant::h2")
    Weather_city_locator = (By.XPATH, ".//*[@class='widget-weather-location-city']")
    Weather_temp_locator = (By.XPATH, ".//*[@class='widget-weather-location-temp']")
    Weather_pressure_locator = (By.XPATH, ".//*[@class='widget-weather-details']//descendant::dd")
    Weather_wind_locator = (By.XPATH, ".//*[@class='widget-weather-details']//descendant::dd[2]")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.current_day = str(datetime.datetime.now())[:11]  # takes only the yyyy-mm-dd values of the date

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.GDPR_locator).click()

    def get_currency_header_name(self):
        os.chdir(r'C:\Users\tzifrea\Desktop\HomePage\Currency')
        print(self.driver.find_element(*self.Currency_header_locator).text+'\n')
        with open(self.current_day + ".txt", "w", encoding="utf-8") as file:
            print(self.driver.find_element(*self.Currency_header_locator).text+'\n', file=file)

    def get_currency_values(self):
        list_of_currencies = self.driver.find_elements(*self.Currency_type_locator)
        for elem in list_of_currencies:
            print(elem.text)
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print(elem.text, file=file)

    def get_weather_header_name(self):
        os.chdir(r'C:\Users\tzifrea\Desktop\HomePage\Weather')
        print(self.driver.find_element(*self.Weather_header_locator).text+'\n')
        with open(self.current_day + ".txt", "w", encoding="utf-8") as file:
            print(self.driver.find_element(*self.Weather_header_locator).text+'\n', file=file)

    def get_weather_values(self):
        self.city = self.driver.find_element(*self.Weather_city_locator).text
        self.temp = self.driver.find_element(*self.Weather_temp_locator).text
        self.pressure = self.driver.find_element(*self.Weather_pressure_locator).text
        self.wind = self.driver.find_element(*self.Weather_wind_locator).text
        print("Valorile vremii in "+self.city+" sunt:"+'\n'+
              "• Temperatura = "+self.temp+'\n'+
              "• Presiunea = "+self.pressure+'\n'+
              "• Vântul = "+self.wind+'\n')
        with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
            print("Valorile vremii in " + self.city + " sunt:" + '\n' +
                  "• Temperatura = " + self.temp + '\n' +
                  "• Presiunea = " + self.pressure + '\n' +
                  "• Vântul = " + self.wind + '\n', file=file)

    def quit(self):
        self.driver.quit()