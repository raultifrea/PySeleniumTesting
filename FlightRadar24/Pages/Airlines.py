from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

class Defs:
    URL = 'https://www.flightradar24.com/data/airlines'
    About_locator = (By.XPATH, "//*[@class='important-banner__footer']//child::button")
    Airlines_locator = (By.XPATH, "//td[@class='notranslate']//a")
    Aircraft_nb_locator = (By.XPATH, "//td[contains(text(),'aircraft')]")


    def __init__(self):
        self.driver = webdriver.Chrome()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.About_locator).click()

    def get_list_of_airlines(self):
        return self.driver.find_elements(*self.Airlines_locator)

    def get_list_of_aircrafts(self):
        return self.driver.find_elements(*self.Aircraft_nb_locator)

    def get_list_of_nb_of_aircrafts(self):
        list_of_nb_aircrafts = [int(x.text[:x.text.find(" ")]) for x in self.get_list_of_aircrafts()]
        # original text ("15 aircrafts"), slices up to the " "
        return list_of_nb_aircrafts

    def get_average_nb_aircrafts(self):
        # noinspection PyTypeChecker
        average_nb_aircrafts_rounded = ("%.1f" % round(np.mean(self.get_list_of_nb_of_aircrafts()), 1))
        #np returns a different type of element, hence the warning
        print("The average number of aircrafts per airline is "+str(average_nb_aircrafts_rounded))

    def get_total_nb_aircrafts(self):
        total_nb_aircrafts = sum(self.get_list_of_nb_of_aircrafts())
        print("The total number of aircrafts is: "+str(total_nb_aircrafts))

    def return_nb_of_airlines(self):
        print("The number of current airlines is: " + str(len(self.get_list_of_airlines())))

    def get_names_of_airlines(self):
        list_of_airlines = [x.text for x in self.get_list_of_airlines()]
        print("The available airlines are: "+', '.join(list_of_airlines))

    def quit(self):
        self.driver.quit()