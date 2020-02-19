import unittest

from personalprojects.Digi24.Pages.Digi24_Home import Defs

class TestCurrency(unittest.TestCase):

    currency = Defs()
    currency.load()
    currency.get_currency_header_name()
    currency.get_currency_values()
    currency.quit()

if __name__ == "__main__":
    unittest.main()