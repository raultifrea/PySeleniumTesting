from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Component:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_to_load(self, locator):
        '''
        :param locator: the locator to wait for
        :return: waits up to 10 seconds for the element to load.
        '''
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))