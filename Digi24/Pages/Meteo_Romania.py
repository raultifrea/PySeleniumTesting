# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime

from selenium.webdriver.common.by import By

class Defs:
    URL = 'https://www.digi24.ro/meteo'
    GDPR_locator = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Pressure_locator = (By.CLASS_NAME, "atmo")
    City_locator = (By.CLASS_NAME, "city")
    Wind_locator = (By.CLASS_NAME, "wind")
    Temperature_locator = (By.CLASS_NAME,"temp")
    Cities_descendant_locator = (By.XPATH, ".//*[@class ='weather-map weather-map-romania']/descendant::button")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.current_day = str(datetime.datetime.now())[:11]  # takes only the yyyy-mm-dd values of the date
        self.pressures_list = []
        self.temperatures_list = []
        self.winds_list = []

    def center_element(self):
        self.driver.execute_script("window.scrollTo(0, 200)")

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.GDPR_locator).click()

    def mmHg_to_psi(self, x):  # converting given atm pressure from mmHg to psi
        formula = int(x) / 51.715
        x = ("%.2f" % round(formula, 2))
        return x

    def pressures(self):
        self.pressure_value = self.driver.find_element(*self.Pressure_locator).text
        self.psi = str(self.mmHg_to_psi(self.pressure_value))
        self.city = self.driver.find_element(*self.City_locator).text
        print("Presiunea atm in " + self.city + " este " + self.psi + " psi")
        with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
            print("Presiunea atm in " + self.city + " este " + self.psi + " psi", file=file)
        if 700 < int(self.pressure_value) < 800:
            self.pressures_list.append(self.psi)
        else:
            print(format(self.city, '*^50'))
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)

    def run_pressures(self):
        list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator)
        for element in list_of_elements:
            element.click()
            self.pressures()

        self.pressures_list = [float(x) for x in self.pressures_list]
        self.pressure_avg = sum(self.pressures_list) / len(self.pressures_list)
        print("\nMedia presiunii atmosferice din Romania este " + str(("%.2f" % round(self.pressure_avg, 2))) + " psi\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia presiunii atmosferice din Romania este " + str(("%.2f" % round(self.pressure_avg, 2))) + " psi\n", file=file)

    def temperatures(self):
        self.temperature_value =self.driver.find_element(*self.Temperature_locator).text
        self.city = self.driver.find_element(*self.City_locator).text
        print("Temperatura din " + self.city + " este " + self.temperature_value + "°C")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("Temperatura din " +self.city + " este " + self.temperature_value + "°C", file=file)
        if len(self.temperature_value) > 0:
            self.temperatures_list.append(self.temperature_value)
        else:
            print(format(self.city, '*^50'))
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)

    def run_temperatures(self):
        list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator)
        for element in list_of_elements:
            element.click()
            self.temperatures()

        self.temperatures_list = [int(x) for x in self.temperatures_list]
        self.temp_avg = sum(self.temperatures_list) / len(self.temperatures_list)
        print("\nMedia temperaturii pe Romania este " + str(("%.2f" % round(self.temp_avg, 2))) + "°C\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia temperaturii pe Romania este " + str(("%.2f" % round(self.temp_avg, 2))) + "°C\n", file=file)

    def ms_to_kmh(self, x):
        formula = int(x) * 3.6
        x = ("%.2f" % round(formula, 2))
        return x

    def winds(self):
        self.wind = self.driver.find_element(*self.Wind_locator).text
        self.city = self.driver.find_element(*self.City_locator).text
        if self.wind == '':
            self.wind = 0
            print(format(self.city, '*^50'))
        self.kmh = str(self.ms_to_kmh(self.wind))
        print("Viteza vantului din " + self.city + " este " + self.kmh + "km/h")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("Viteza vantului din " + self.city + " este " + self.kmh + "km/h", file=file)
        if int(self.wind) > -1:
            self.winds_list.append(self.kmh)
        else:
            print(format(self.city, '*^50'))

    def run_winds(self):
        list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator)
        for element in list_of_elements:
            element.click()
            self.winds()

        self.winds_list = [float(x) for x in self.winds_list]
        self.wind_avg = sum(self.winds_list) / len(self.winds_list)
        print("\nMedia vitezei vantului in Romania este " + str(("%.2f" % round(self.wind_avg, 2))) + " km\h\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia vitezei vantului in Romania este " + str(("%.2f" % round(self.wind_avg, 2))) + " km\h\n",
                  file=file)

    def quit(self):
        self.driver.quit()





