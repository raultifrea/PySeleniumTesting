# -*- coding: utf-8 -*-
import unittest, HtmlTestRunner
from Digi24.Components.Report_Path import report_path_meteo_workbench
from Digi24.Pages.Digi24_Meteo import Defs


class TestMeteoTemperaturesBanat(unittest.TestCase):
    def test_meteo_temperature_Banat(self):
        meteo_transilvania = Defs()
        meteo_transilvania.load()
        meteo_transilvania.get_Regions("BANAT")
        meteo_transilvania.run_temperatures()
        meteo_transilvania.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_meteo_workbench))


