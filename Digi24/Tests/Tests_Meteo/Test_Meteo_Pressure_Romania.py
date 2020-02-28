# -*- coding: utf-8 -*-
import unittest, HtmlTestRunner
from Digi24.Components.Report_Path import report_path_meteo_workbench
from Digi24.Pages.Digi24_Meteo import Defs

from Digi24.Pages.Digi24_Meteo import Defs


class TestMeteoPressureRomania(unittest.TestCase):
    def test_meteo_pressure_Romania(self):
        meteo_romania = Defs()
        meteo_romania.load()
        meteo_romania.center_element()
        meteo_romania.run_pressures()
        meteo_romania.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_meteo_workbench))


