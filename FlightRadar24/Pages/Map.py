from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    Settings_Map_MapStyle_dropdown_locator = (By.XPATH, '//*[@id="fr24_mapType"]/button')
    Settings_Map_MapStyle_list_locator = (By.XPATH, "//*[@id='fr24_mapType']//descendant::a")
    Settings_Map_ATCBoundaries_dropdown_locator = (By.XPATH, '//*[@id="fr24_showATC"]/button')
    Settings_Map_ATCBoundaries_list_locator = (By.XPATH, '//*[@id="fr24_showATC"]//descendant::a')
    Settings_Map_Aeronautical_Charts_dropdown_locator = (By.XPATH, '//*[@id="fr24_showNavdataLayer"]/button')
    Settings_Map_Aeronautical_Charts_list_locator = (By.XPATH, '//*[@id="fr24_showNavdataLayer"]//descendant::a')
    Settings_Map_Aircraft_Size_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftSize"]/button')
    Settings_Map_Aircraft_Size_list_locator = (By.XPATH, '//*[@id="fr24_aircraftSize"]//descendant::a')
    Settings_Map_Brightness_slidebar_locator = (By.XPATH, '//*[@id="fr24_Brightness"]/div')
    Settings_Map_Brightness_slider_locator = (By.XPATH, '//*[@id="fr24_Brightness"]/a')
    Settings_Map_toggles_locator = (By.XPATH, "//*[@id='mapsettings']//div[contains(@class,'toggle')]")
    Settings_Map_airport_pin_visibility_slidebar_locator = (By.XPATH, '//*[@id="fr24_airportDensity"]/div')
    Settings_Map_airport_pin_visibility_slider_locator = (By.XPATH, '//*[@id="fr24_airportDensity"]/a')
    Settings_dropdown_default_values_locator = (By.XPATH, "//button[@data-toggle='dropdown']")
    iframe_locator = (By.XPATH, '//*[@id="map_canvas"]/div/div/iframe')
    subscription_plan_locator = (By.XPATH, "//*[@class='subscription']")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def switch_to_frame(self):
        self.driver.switch_to.frame(2)

    @property
    def brigthness_button_slidebar(self):
        # defines the slide bar
        return self.driver.find_element(*self.Settings_Map_Brightness_slidebar_locator)

    @property
    def brightness_button_slider(self):
        #defines the slider circle
        return self.driver.find_element(*self.Settings_Map_Brightness_slider_locator)

    @property
    def airport_pin_visilibity_slidebar(self):
        #defines the slide bar
        return self.driver.find_element(*self.Settings_Map_airport_pin_visibility_slidebar_locator)

    @property
    def airport_pin_visilibity_slider(self):
        #defines the slider circle
        return self.driver.find_element(*self.Settings_Map_airport_pin_visibility_slider_locator)

    def slidebar_width(self):
        #defines the slide bar's width value as integer (21)
        self.width = self.airport_pin_visilibity_slidebar.size['width']
        #same width as for brightness slidebar, no extra locator needed
        return self.width

    def move(self):
        move = ActionChains(self.driver)
        return move

    def drag_and_drop_slider(self, percent: int, slider):
        #drags and drops the given slider (brightness or pin visibility) on the slide bar by a given percent integer
        self.move().click_and_hold(slider).move_by_offset(percent * self.slidebar_width() / 100, 0).release().perform()

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

    def get_list_of_default_dropdown_values(self):
        #returns a list of the default drop-down web elements from the Settings menu
        return self.driver.find_elements(*self.Settings_dropdown_default_values_locator)

    def get_list_of_default_dropdown_values_strings(self):
        #returns a list of the default drop-down strings from the Settings menu
        return [element.text for element in self.get_list_of_default_dropdown_values()]

    def check_dropdown_functionality_old(self, the_list, option: str):
        #checks whether the selected dropdown value is saved in the header
        self.check_dropdown_functionality(the_list(), option)
        assert option in self.get_list_of_default_dropdown_values_strings(), f"option: {option} is not saved correctly"

    def check_dropdown_functionality(self, the_list: list, click):
        '''
        :param the_list: the list of all elements in a dropdown list (e.g. get_list_of_map_styles)
        :param click: clicks the button pertaining to the same dropdown list (e.g. click_map_style_button)
        :return: checks whether each dropdown value is saved in the header, one at a time
        '''
        for element in the_list:
            element.click()
            assert element.text in self.get_list_of_default_dropdown_values_strings(), f"option: {element.text} is not saved correctly"
            click()

    @property
    def map_style_button(self):
        return self.driver.find_element(*self.Settings_Map_MapStyle_dropdown_locator)

    def click_map_style_button(self):
        self.map_style_button.click()

    def get_list_of_map_styles(self):
        #returns a list of dropdown values from the Map Style options of the Map tab
        return self.driver.find_elements(*self.Settings_Map_MapStyle_list_locator)

    @property
    def atc_boundaries_button(self):
        return self.driver.find_element(*self.Settings_Map_ATCBoundaries_dropdown_locator)

    def click_atc_boundaries_button(self):
        self.atc_boundaries_button.click()

    def get_list_of_atc_boundaries(self):
        #returns a list of dropdown values from the ATC Boundaries of the Map tab
        return self.driver.find_elements(*self.Settings_Map_ATCBoundaries_list_locator)

    @property
    def aeronautical_charts_button(self):
        return self.driver.find_element(*self.Settings_Map_Aeronautical_Charts_dropdown_locator)

    def click_aeronautical_charts_button(self):
        self.aeronautical_charts_button.click()

    def get_list_of_aeronautical_charts(self):
        #returns a list of dropdown values from the Aeronautical Charts of the Map tab
        return self.driver.find_elements(*self.Settings_Map_Aeronautical_Charts_list_locator)

    @property
    def aircraft_sizes_button(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Size_dropdown_locator)

    def get_list_of_aircraft_sizes(self):
        #returns a list of dropdown values from the Aircraft sizes of the Map tab
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Size_list_locator)

    def click_aircraft_sizes_button(self):
        self.aircraft_sizes_button.click()

    def get_list_of_toggles(self):
        return self.driver.find_elements(*self.Settings_Map_toggles_locator)

    def change_toggle_button_state(self, option: str):
        for element in self.get_list_of_toggles():
            if element.get_attribute('id') == option:
                element.click()
                time.sleep(3)

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

    def wait_for_login_refresh(self):
        #waits up to 10 seconds for the subscription to be updated after login. Can be changed to accept  argument
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.subscription_plan_locator))

    def quit(self):
        self.driver.quit()
