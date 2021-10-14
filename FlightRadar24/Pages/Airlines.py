from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import time

from FlightRadar24.Components.Components import Component


class Defs(Component):
    URL = 'https://www.flightradar24.com/data/airlines'
    About_locator = (By.XPATH, "//*[@class='important-banner__footer']//child::button")
    Airlines_locator = (By.XPATH, "//td[@class='notranslate']//a")
    Airlines_aircraft_locator = (By.XPATH, ".//following::td[2]") #//td[contains(text(),'aircraft')]"
    Aircraft_nb_locator = (By.XPATH, "//td[contains(text(),'aircraft')]")
    Summer_Popup_close_button_locator = (By.XPATH, '//*[@id="subscription-promo-close"]')
    AZ_buttons_locator = (By.XPATH, "//th[@class='text-right']//child::a")

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.wait_for_element_to_be_clickable(self.About_locator)
        self.click_about_button()
        # self.click_summer_popup_close_button()

    def get_list_of_az_buttons(self):
        return self.driver.find_elements(*self.AZ_buttons_locator)

    def click_selected_letter(self, letter: str):
        for element in self.get_list_of_az_buttons():
            if element.text == letter.upper():
                element.click()
                break

    @property
    def about_button(self):
        return self.driver.find_element(*self.About_locator)

    def click_about_button(self):
        self.about_button.click()

    @property
    def summer_popup_close_button(self):
        return self.driver.find_element(*self.Summer_Popup_close_button_locator)

    def click_summer_popup_close_button(self):
        self.summer_popup_close_button.click()

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

    def get_number_of_aircrafts_per_airline(self, airline: str):
        '''
        :param airline: the airline to get number of aircraft
        :return: prints the airline name and the number of aircraft available for it
        :rtype: string
        '''
        for element in self.get_list_of_airlines():
            if element.text == airline:
                print(element.text + " has " + element.find_element(*self.Airlines_aircraft_locator).text)

    def quit(self):
        self.driver.quit()