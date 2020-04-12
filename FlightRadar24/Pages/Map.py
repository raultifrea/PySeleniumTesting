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

    def __init__(self):
        self.driver = webdriver.Chrome()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.About_locator).click()

    def login(self):
        email = self.driver.find_element(*self.Email_locator)
        password = self.driver.find_element(*self.Password_locator)
        self.driver.find_element(*self.LogIn_locator).click()
        email.click()
        email.send_keys("raoul_tifrea@yahoo.com")
        password.click()
        password.send_keys("nokianseries")
        self.driver.find_element(*self.SignIn_locator).click()


    def quit(self):
        self.driver.quit()