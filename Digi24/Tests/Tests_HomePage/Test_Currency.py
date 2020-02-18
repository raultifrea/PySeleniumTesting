import unittest

from personalprojects.Digi24.Pages.Digi24_Home import Defs

class TestCurrency(unittest.TestCase):

    currency = Defs()
    currency.load()
    currency.get_header_name()
    currency.quit()

if __name__ == "__main__":
    unittest.main()