from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Component:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def wait_to_load(self, locator):
        '''
        :param locator: the locator to wait for
        :return: waits up to 10 seconds for the element to load.
        '''
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator1, locator2=''):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator1))
        except TimeoutException:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator2))

    def wait_for_text_to_change(self, element: WebElement):
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

    def click_button_multiple_times(self, button, times: int):
        '''
        :param button: the "click" button to click each time
        :param times: the number of times to click the button
        :return: clicks the mentioned button for the mentioned number of times
        '''
        for element in range(times):
            button()
