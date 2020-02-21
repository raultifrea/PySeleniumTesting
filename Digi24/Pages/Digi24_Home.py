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
    Article_title_locator = (By.XPATH, ".//*[@class='article-title']//a")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.current_day = str(datetime.datetime.now())[:11]  # takes only the yyyy-mm-dd values of the date

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.GDPR_locator).click()

    def get_currency_header_name(self):
        #os.chdir(r'C:\Users\tzifrea\Desktop\HomePage\Currency')
        os.chdir(r'C:\Users\F73482\Desktop\HomePage\Currency')
        self.currency_header = self.driver.find_element(*self.Currency_header_locator).text
        print(self.currency_header+'\n')
        with open(self.current_day + ".txt", "w", encoding="utf-8") as file:
            print(self.currency_header+'\n', file=file)
        assert self.currency_header == "CURS VALUTAR", "Incorrect weather header tittle"

    def get_currency_values(self):
        list_of_currencies = self.driver.find_elements(*self.Currency_type_locator)
        for elem in list_of_currencies:
            print(elem.text)
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print(elem.text, file=file)
            assert len(elem.text) > 0, "No value for currency"

    def get_weather_header_name(self):
        #os.chdir(r'C:\Users\tzifrea\Desktop\HomePage\Weather')
        os.chdir(r'C:\Users\F73482\Desktop\HomePage\Weather')
        self.weather_header = self.driver.find_element(*self.Weather_header_locator).text
        print(self.weather_header+'\n')
        with open(self.current_day + ".txt", "w", encoding="utf-8") as file:
            print(self.weather_header+'\n', file=file)
        assert self.weather_header == "VREMEA", "Incorrect weather header tittle"

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
        assert len(self.temp) > 0, "No value present for temperature"
        assert len(self.pressure) > 0, "No value present for temperature"
        assert len(self.wind) > 0, "No value present for temperature"

    def get_articles_titles(self):
        # os.chdir(r'C:\Users\tzifrea\Desktop\HomePage\Currency')
        os.chdir(r'C:\Users\F73482\Desktop\HomePage\Articles')
        list_of_articles_titles = self.driver.find_elements(*self.Article_title_locator)
        for elem in list_of_articles_titles:
            print(elem.text)
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print(elem.text, file=file)
            assert len(elem.text) > 0, str(elem) + "Article title is empty"

    def quit(self):
        self.driver.quit()