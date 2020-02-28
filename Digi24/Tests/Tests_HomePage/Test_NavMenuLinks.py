import unittest, HtmlTestRunner

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Components.Report_Path import report_path_homepage_workbench
from Digi24.Pages.Digi24_Home import Defs

class TestNavMenuLinks(unittest.TestCase):

    def test_navmenulinks(self):
        navMenuLinks = Defs()
        navMenuLinks.load()
        navMenuLinks.click_Nav_Menu_button()
        navMenuLinks.get_nav_menu_links()
        navMenuLinks.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_homepage_workbench))
