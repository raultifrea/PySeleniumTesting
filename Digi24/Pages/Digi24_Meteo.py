# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime, os

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Defs:
    URL = 'https://www.digi24.ro/meteo'
    GDPR_locator = (By.XPATH, ".//*[@class='gdpr-button gdpr-trigger']")
    Pressure_locator = (By.CLASS_NAME, "atmo")
    City_locator = (By.CLASS_NAME, "city")
    Wind_locator = (By.CLASS_NAME, "wind")
    Temperature_locator = (By.CLASS_NAME,"temp")
    Cities_descendant_locator_Romania = (By.XPATH, ".//*[@class ='weather-map weather-map-romania']/descendant::button")
    Cities_descendant_locator_Transilvania = (By.XPATH, ".//*[@class ='weather-map weather-map-transilvania']/descendant::button")
    Cities_descendant_locator_Banat = (By.XPATH,".//*[@class ='weather-map weather-map-banat']/descendant::button")
    Cities_descendant_locator_Crisana = (By.XPATH, ".//*[@class ='weather-map weather-map-crisana']/descendant::button")
    Cities_descendant_locator_Maramures = (By.XPATH, ".//*[@class ='weather-map weather-map-maramures']/descendant::button")
    Cities_descendant_locator_Dobrogea = (By.XPATH, ".//*[@class ='weather-map weather-map-dobrogea']/descendant::button")
    Cities_descendant_locator_Oltenia = (By.XPATH, ".//*[@class ='weather-map weather-map-oltenia']/descendant::button")
    Cities_descendant_locator_Muntenia = (By.XPATH, ".//*[@class ='weather-map weather-map-muntenia']/descendant::button")
    Cities_descendant_locator_Moldova = (By.XPATH, ".//*[@class ='weather-map weather-map-moldova']/descendant::button")
    Regions_descendant_locator = (By.XPATH, ".//*[@class='dropdown-list-item']/following-sibling::li")
    Active_Region_locator = (By.XPATH, ".//*[@class='dropdown-list-item-link active']")
    #Ad_locator = (By.XPATH, ".//*[@class='amp-animate amp-mode-mouse']")

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

    def get_Regions(self, region):
        list_of_regions = self.driver.find_elements(*self.Regions_descendant_locator)
        for element in list_of_regions:
            if region == element.text:
                element.click()
                break

    def get_Cities_descendants(self, argument): #placeholder argument for the pressures,temperatures,winds methods
        self.active_region = self.driver.find_element(*self.Active_Region_locator).text
        if self.active_region == 'TRANSILVANIA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Transilvania')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Transilvania')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Transilvania)
        elif self.active_region == 'BANAT':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Banat')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Banat')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Banat)
        elif self.active_region == 'CRIȘANA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Crisana')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Crisana')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Crisana)
        elif self.active_region == 'MARAMUREȘ':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Maramures')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Maramures')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Maramures)
        elif self.active_region == 'DOBROGEA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Dobrogea')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Dobrogea')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Dobrogea)
        elif self.active_region == 'OLTENIA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Oltenia')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Oltenia')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Oltenia)
        elif self.active_region == 'MUNTENIA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Muntenia')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Muntenia')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Muntenia)
        elif self.active_region == 'MOLDOVA':
            #os.chdir(r'C:\Users\tzifrea\Desktop\Meteo\Moldova')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo\Moldova')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Moldova)
        else:
            # os.chdir(r'C:\Users\tzifrea\Desktop\Meteo')
            os.chdir(r'C:\Users\F73482\Desktop\Meteo')
            list_of_elements = self.driver.find_elements(*self.Cities_descendant_locator_Romania)
        for element in list_of_elements:
            element.click()
            argument()

    def mmHg_to_psi(self, x):  # converting given atm pressure from mmHg to psi
        formula = int(x) / 51.715
        x = ("%.2f" % round(formula, 2))
        return x

    def pressures(self):
        self.pressure_value = self.driver.find_element(*self.Pressure_locator).text
        self.city = self.driver.find_element(*self.City_locator).text
        if self.pressure_value == '':
            self.pressure_value = 0
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)
        else:
            self.psi = str(self.mmHg_to_psi(self.pressure_value))
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print("Presiunea atm în " + self.city + " este " + self.psi + " psi", file=file)
            if 700 < int(self.pressure_value) < 800:
                self.pressures_list.append(self.psi)
            else:
                with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                    print(format(self.city, '*^50'), file=file)

    def run_pressures(self):
        self.get_Cities_descendants(self.pressures)
        self.pressures_list = [float(x) for x in self.pressures_list]
        self.pressure_avg = sum(self.pressures_list) / len(self.pressures_list)
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia presiunii atmosferice din " + self.active_region + " este " + str(("%.2f" % round(self.pressure_avg, 2))) + " psi\n", file=file)
        os.chdir(r'D:')

    def temperatures(self):
        self.temperature_value = self.driver.find_element(*self.Temperature_locator).text
        self.city = self.driver.find_element(*self.City_locator).text
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("Temperatura din " +self.city + " este " + self.temperature_value + "°C", file=file)
        if len(self.temperature_value) > 0:
            self.temperatures_list.append(self.temperature_value)
        else:
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)

    def run_temperatures(self):
        self.get_Cities_descendants(self.temperatures)
        self.temperatures_list = [int(x) for x in self.temperatures_list]
        self.temp_avg = sum(self.temperatures_list) / len(self.temperatures_list)
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia temperaturii din " + self.active_region + " este " + str(("%.2f" % round(self.temp_avg, 2))) + "°C\n", file=file)
        os.chdir(r'D:')

    def ms_to_kmh(self, x):
        formula = int(x) * 3.6
        x = ("%.2f" % round(formula, 2))
        return x

    def winds(self):
        self.wind_value = self.driver.find_element(*self.Wind_locator).text
        self.city = self.driver.find_element(*self.City_locator).text
        if self.wind_value == '':
            self.wind_value = 0
        self.kmh = str(self.ms_to_kmh(self.wind_value))
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("Viteza vântului din " + self.city + " este " + self.kmh + "km/h", file=file)
        if int(self.wind_value) > -1:
            self.winds_list.append(self.kmh)
        else:
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print(format(self.city, '*^50'), file=file)

    def run_winds(self):
        self.get_Cities_descendants(self.winds)
        self.winds_list = [float(x) for x in self.winds_list]
        self.wind_avg = sum(self.winds_list) / len(self.winds_list)
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia vitezei vântului din " + self.active_region + " este " + str(("%.2f" % round(self.wind_avg, 2))) + " km/h\n", file=file)
        os.chdir(r'D:')

    def quit(self):
        self.driver.quit()






