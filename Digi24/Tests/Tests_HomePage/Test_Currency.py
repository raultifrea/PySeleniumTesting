import unittest, HtmlTestRunner

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Components.Report_Path import report_path_homepage_workbench
from Digi24.Pages.Digi24_Home import Defs


class TestCurrency(unittest.TestCase):

    def test_currency(self):
        currency = Defs()
        currency.load()
        currency.get_currency_header_name()
        currency.get_currency_values()
        currency.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_homepage_workbench))
