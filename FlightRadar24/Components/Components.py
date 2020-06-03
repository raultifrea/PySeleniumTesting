from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import time

class Component:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_to_load(self, locator):
        '''
        :param locator: the locator to wait for
        :return: waits up to 10 seconds for the element to load.
        '''
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator1, locator2):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator1))
        except TimeoutException:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator2))

    def wait_for_text_to_change(self, element: WebElement):
        '''
        :param element: the web element whose text to wait for
        :return: waits upt to 10 seconds for the element's text to change, otherwise is breaks
        '''
        original_value = element.text
        while original_value == element.text:
            WebDriverWait(self.driver, 10)
            #break
        else:
            return element

    def slidebar_width(self, slidebar: WebElement):
        '''
        :param slidebar: the slidebar webelement to calculate its width
        :return: returns the slide bar's width value as integer
        '''
        return slidebar.size['width']

    def move(self):
        move = ActionChains(self.driver)
        return move

    def drag_and_drop_slider(self, percent: int, slider: WebElement, slidebar: WebElement):
        '''
        :param percent: the percent to which the slider is dragged
        :param slider: the slider webelement circle button to drag
        :param slidebar: the slidebar webelement to take into account
        :return: drags and drops the given slider on the slide bar by a given percent integer
        '''
        self.move().click_and_hold(slider).move_by_offset(percent * self.slidebar_width(slidebar) / 100, 0).release().perform()