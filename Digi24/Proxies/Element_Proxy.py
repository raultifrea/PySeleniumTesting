from typing import Iterator

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

from pte_selenium.proxies.locator import Locator


class ElementProxy:
    def __init__(self, element: WebElement):
        self.element = element
        return

    @property
    def get_text(self):
        return self.element.text

    @property
    def is_displayed(self):
        return self.element.is_displayed()

    def find_element(self, locator: Locator) -> __init__:
        element = self.element.find_element(locator.strategy, locator.selector)
        return ElementProxy(element)

    def find_elements(self, locator: Locator) -> Iterator[__init__]:
        return (
            ElementProxy(element)
            for element in self.element.find_elements(locator.strategy, locator.selector)
        )

    def click(self):
        self.element.click()

    def send_keys(self, value: str):
        self.element.send_keys(value)

    def get_attr(self, attr: str) -> str:
        return self.element.get_attribute(attr)

    def location(self):
        return self.element.location

