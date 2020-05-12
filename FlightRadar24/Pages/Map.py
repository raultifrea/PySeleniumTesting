from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Defs:
    URL = 'https://www.flightradar24.com'
    About_locator = (By.XPATH, "//*[@class='important-banner__footer']//child::button")
    LogIn_locator = (By.XPATH, "//*[@class='dropdown-toggle logout']")
    Email_locator = (By.XPATH, "//*[@id='fr24_SignInEmail']")
    Password_locator = (By.XPATH, "//*[@id='fr24_SignInPassword']")
    SignIn_locator = (By.XPATH, "//*[@id='fr24_SignIn']")
    Login_text_locator = (By.XPATH, "//*[contains(text(),'Login authorization succeeded')]")
    Settings_button_locator = (By.XPATH, "//*[@id='fr24_SettingsMenu']")
    Settings_Map_MapStyle_dropdown_button_locator = (By.XPATH, "//*[@class='btn btn-default dropdown-toggle pull-right']")
    Settings_Map_MapStyle_list_locator = (By.XPATH, "//*[@id='fr24_mapType']//descendant::a")

    def __init__(self):
        self.driver = webdriver.Chrome()



    @property
    def email_button(self):
        return self.driver.find_element(*self.Email_locator)

    def click_email_button(self):
        self.email_button.click()

    def send_keys_email_button(self, key: str):
        self.email_button.clear()
        self.email_button.send_keys(key)

    @property
    def password_button(self):
        return self.driver.find_element(*self.Password_locator)

    def click_password_button(self):
        self.password_button.click()

    def send_keys_password_button(self, key: str):
        self.password_button.clear()
        self.password_button.send_keys(key)

    @property
    def login_button(self):
        return self.driver.find_element(*self.LogIn_locator)

    def click_login_button(self):
        self.login_button.click()

    @property
    def sign_in_button(self):
        return self.driver.find_element(*self.SignIn_locator)

    def click_sign_in_button(self):
        self.sign_in_button.click()

    @property
    def settings_button(self):
        return self.driver.find_element(*self.Settings_button_locator)

    def click_settings_button(self):
        self.settings_button.click()

    @property
    def map_style_button(self):
        return self.driver.find_element(*self.Settings_Map_MapStyle_dropdown_button_locator)

    def click_map_style_button(self):
        self.map_style_button.click()

    def get_list_of_map_styles(self):
        #returns a list of dropdown values from the Map Style options of the Map tab
        return self.driver.find_elements(*self.Settings_Map_MapStyle_list_locator)

    def click_selected_map_style(self, option: str):
        for element in self.get_list_of_map_styles():
            if element.text == option:
                element.click()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.About_locator).click()

    def login(self):
        self.click_login_button()
        self.click_email_button()
        self.send_keys_email_button("raoul_tifrea@yahoo.com")
        self.click_password_button()
        self.send_keys_password_button("nokianseries")
        self.click_sign_in_button()

    def check_map_style_functionality(self, option: str):
        #checks whether the selected map style name from the dropdown list is saved in the header
        self.click_settings_button()
        self.click_map_style_button()
        self.click_selected_map_style(option)
        assert self.map_style_button.text == option, "Map Style option is not saved correctly"

    def quit(self):
        self.driver.quit()
