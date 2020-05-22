from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
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

    def slidebar_width(self, slidebar: WebElement):
        '''
        :param slidebar: the slidebar webelement to calculate its width
        :return: returns the slide bar's width value as integer
        '''
        return slidebar.size['width']