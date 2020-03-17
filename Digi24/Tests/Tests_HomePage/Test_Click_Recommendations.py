import unittest, HtmlTestRunner

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Components.Report_Path import report_path_homepage_workbench
from Digi24.Pages.Digi24_Home import Defs

class TestRecommendations(unittest.TestCase):

    def test_weather(self):
        recommendations = Defs()
        recommendations.load()
        recommendations.click_days_of_the_week()
        recommendations.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_homepage_workbench))
