# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime, time

from selenium.webdriver.common.by import By

from Digi24.Proxies.Element_Proxy import ElementProxy
from Digi24.Proxies.Locator import Locator


class Defs:
    URL = 'https://www.digi24.ro/meteo'
    GDPR_locator = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Pressure_locator = Locator(By.CLASS_NAME, "atmo")
    City_locator = (By.CLASS_NAME, "city")
    Wind_locator = (By.CLASS_NAME, "wind")
    Temperature_locator = (By.CLASS_NAME,"temp")

    @property
    def pressure(self) -> ElementProxy:
        return self.driver.find_element(self.Pressure_locator)

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

    def pressure(self):
        self.pressure_value = self.driver.find_element(self.Pressure_locator).text
        #self.pressure_value = self.driver.find_element(By.CLASS_NAME, "atmo").text
        self.psi = str(self.mmHg_to_psi(self.pressure_value))
        self.city = self.driver.find_element(By.CLASS_NAME, "city").text
        print("Presiunea atm in " + self.city + " este " + self.psi + " psi")
        with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
            print("Presiunea atm in " + self.city + " este " + self.psi + " psi", file=file)
        if 700 < int(self.pressure_value) < 800:
            self.pressures_list.append(self.psi)
        else:
            print(format(self.city, '*^50'))
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)

    def run_pressure(self):
        for x in range(1, 14):  # goes through all the cities on the map based on descendants
            self.driver.find_element_by_xpath(".//*[@class='weather-map weather-map-romania']/descendant::button[{0}]".format(str(x))).click()
            self.pressure()

        self.pressures_list = [float(x) for x in self.pressures_list]
        self.pressure_avg = sum(self.pressures_list) / len(self.pressures_list)
        print("\nMedia presiunii atmosferice din Romania este " + str(("%.2f" % round(self.pressure_avg, 2))) + " psi\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia presiunii atmosferice din Romania este " + str(("%.2f" % round(self.pressure_avg, 2))) + " psi\n", file=file)

    def quit(self):
        self.driver.quit()






