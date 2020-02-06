# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

class Test_Meteo_Romania(unittest.TestCase):
    pressures_list = []
    temperatures_list = []
    winds_list= []
    os.chdir(r'C:\Users\tzifrea\Desktop\Meteo')
    current_day = str(datetime.datetime.now())[:11] #takes only the yyyy-mm-dd values of the date
    open(current_day + ".txt", "w").close() #deletes content before running the script again
    with open(current_day + ".txt", 'a+', encoding="utf-8") as file:
        print("Timestamp: "+str(datetime.datetime.now())[:19]+"\n",file=file)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.digi24.ro/meteo")
        self.driver.find_element_by_xpath(".//*[@class='gdpr-button gdpr-trigger']").click()  # GDPR prompt dismissal
        center_element = self.driver.find_element_by_xpath(".//*[@class='weather-map-pin weather-map-pin-sibiu']") #finds a central element on the page
        actions = ActionChains(self.driver)
        actions.move_to_element(center_element).perform() #scrolls the page to the central element

    def test_atm_pressures(self):
        driver = self.driver
        def mmHg_to_psi(x): #converting given atm pressure from mmHg to psi
            formula = int(x) / 51.715
            x = ("%.2f" % round(formula,2))
            return x

        def pressure():
            pressure = driver.find_element_by_class_name("atmo").text
            psi = str(mmHg_to_psi(pressure))
            city = driver.find_element_by_class_name("city").text
            print("Presiunea atm in " + city + " este " + psi + " psi")
            with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                print("Presiunea atm in " + city + " este " + psi + " psi",file=file)
            if 700 < int(pressure) < 800:
                self.pressures_list.append(psi)
            else:
                print(format(city, '*^50'))
                with open(self.current_day + ".txt", 'a+', encoding="utf-8") as file:
                    print(format(city, '*^50'),file=file)

        for x in range(1,14): #goes through all the cities on the map based on descendants
            driver.find_element_by_xpath(".//*[@class='weather-map weather-map-romania']/descendant::button[{0}]".format(str(x))).click()
            pressure()

        self.pressures_list = [float(x) for x in self.pressures_list]
        pressure_avg = sum(self.pressures_list) / len(self.pressures_list)
        print("\nMedia presiunii atmosferice din Romania este "+str(("%.2f" % round(pressure_avg,2)))+" psi\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia presiunii atmosferice din Romania este " + str(("%.2f" % round(pressure_avg, 2))) + " psi\n",file=file)

    def test_temperatures(self):
        driver = self.driver

        def temperatures():
            temperature = driver.find_element_by_class_name("temp").text
            city = driver.find_element_by_class_name("city").text
            print("Temperatura din " + city + " este " + temperature + "°C")
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print("Temperatura din " + city + " este " + temperature + "°C",file=file)
            if len(temperature)>0:
                self.temperatures_list.append(temperature)
            else:
                print(format(city, '*^50'))
                with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                    print(format(city, '*^50'),file=file)

        for x in range(1, 14): #goes through all the cities on the map based on descendants
            driver.find_element_by_xpath(".//*[@class='weather-map weather-map-romania']/descendant::button[{0}]".format(str(x))).click()
            temperatures()

        self.temperatures_list = [int(x) for x in self.temperatures_list]
        temp_avg = sum(self.temperatures_list) / len(self.temperatures_list)
        print("\nMedia temperaturii pe Romania este " + str(("%.2f" % round(temp_avg, 2)))+"°C\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia temperaturii pe Romania este " + str(("%.2f" % round(temp_avg, 2))) + "°C\n",file=file)

    def test_wind(self):
        driver = self.driver
        def ms_to_kmh(x):
            formula = int(x) * 3.6
            x = ("%.2f" % round(formula,2))
            return x

        def winds():
            wind = driver.find_element_by_class_name("wind_value").text
            city = driver.find_element_by_class_name("city").text
            if wind =='':
                wind = 0
                print(format(city, '*^50'))
            kmh = str(ms_to_kmh(wind))
            print("Viteza vantului din " + city + " este " + kmh + "km/h")
            with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
                print("Viteza vantului din " + city + " este " + kmh + "km/h",file=file)
            if int(wind) > -1:
                self.winds_list.append(kmh)
            else:
                print(format(city, '*^50'))

        for x in range(1, 14): #goes through all the cities on the map based on descendants
            driver.find_element_by_xpath(".//*[@class='weather-map weather-map-romania']/descendant::button[{0}]".format(str(x))).click()
            winds()

        self.winds_list = [float(x) for x in self.winds_list]
        wind_avg = sum(self.winds_list) / len(self.winds_list)
        print("\nMedia vitezei vantului in Romania este " + str(("%.2f" % round(wind_avg, 2)))+" km\h\n")
        with open(self.current_day + ".txt", "a+", encoding="utf-8") as file:
            print("\nMedia vitezei vantului in Romania este " + str(("%.2f" % round(wind_avg, 2))) + " km\h\n",file=file)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
