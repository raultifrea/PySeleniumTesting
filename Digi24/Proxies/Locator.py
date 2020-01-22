from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class Locator:
    strategy: By
    selector: str
