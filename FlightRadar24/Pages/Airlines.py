from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

class Defs:
    URL = 'https://www.flightradar24.com/data/airlines'
    About_locator = (By.XPATH, "//*[@class='important-banner__footer']//child::button")
    Number_of_aircraft_locator = (By.XPATH, "// td[contains(text(), 'aircraft')]")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.About_locator).click()

    def get_average_nb_aircrafts(self):
        list_of_nb_aircrafts_elements=self.driver.find_elements(*self.Number_of_aircraft_locator)
        list_of_nb_aircrafts = [int(x.text[:x.text.find(" ")]) for x in list_of_nb_aircrafts_elements] # original text ("15 aircrafts"), slices up to the " "
        average_nb_aircrafts = np.mean(list_of_nb_aircrafts)
        average_nb_aircrafts_rounded = ("%.1f" % round(average_nb_aircrafts, 1)) #np returns a different type of element, hence the warning
        print("The average number of aircrafts per airline is "+str(average_nb_aircrafts_rounded))

    def quit(self):
        self.driver.quit()