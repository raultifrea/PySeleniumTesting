import unittest, HtmlTestRunner

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Components.Report_Path import report_path_homepage_workbench
from Digi24.Pages.Digi24_Home import Defs

class TestWeather(unittest.TestCase):

    def test_weather(self):
        weather = Defs()
        weather.load()
        weather.get_weather_header_name()
        weather.get_weather_values()
        weather.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_homepage_workbench))
